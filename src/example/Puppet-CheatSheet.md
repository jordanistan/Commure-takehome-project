Puppet Cheat Sheet

Commands:
```bash
puppet apply: Runs the Puppet agent on the local system and applies any changes specified in the Puppet manifests.
puppet agent: Runs the Puppet agent on the local system and connects to the Puppet master to retrieve and apply any updates.
puppet resource: Allows you to inspect and modify system resources (e.g., files, services, packages) using the Puppet resource type syntax.
puppet module install: Installs a specific Puppet module from the Puppet Forge or a custom source.
puppet parser validate: Validates the syntax of a Puppet manifest or module.
puppet cert list: Lists all of the certificate requests and their status on the Puppet master.
puppet cert sign: Signs a certificate request on the Puppet master, allowing the agent to connect and receive updates.
puppet config print: Prints the current settings for a specific Puppet configuration option.
puppet filebucket: Allows you to backup and restore files managed by Puppet.
puppet node clean: Cleans all data associated with a node from the Puppet master, allowing the node to be provisioned again.
```

## Manifests:

Manifests are written in Puppet's domain-specific language (DSL) and are used to define the desired state of a system.
The entry point for a manifest is the site.pp file located in the manifests directory.
Manifests are organized using a resource-type-based syntax, where resources are defined using a type (e.g., file, package, service) followed by a name and a set of attributes.
Manifests can also include conditionals and variables to make them more dynamic.

## Modules:

Modules are collections of manifests, files, and templates that are used to manage specific aspects of a system.
Modules are typically organized by functionality, such as a "ntp" module for managing the NTP service, or a "java" module for managing Java installations.
Modules can be installed from the Puppet Forge or created locally.

## Hiera:

Hiera is a key-value data store that can be used to separate data from code in a Puppet manifest.
Hiera allows you to define data in a hierarchical structure, where data is looked up based on the current node's "Facter" facts.
Hiera is typically used to manage common data such as users, packages, and services across multiple nodes.

## Facter:

Facter is a command-line tool that retrieves system facts, such as IP address, hostname, and operating system version.
Facter facts can be used in Puppet manifests to make them more dynamic and node-specific.
Overall, Puppet is a powerful tool for automating system configuration management and allows you to maintain consistency across multiple nodes. With a little bit of practice, you can use it to manage your infrastructure effectively.


The following is an example of a Puppet script that can be used to check for vulnerabilities on a Linux system:

```bash
# Define a task to run the `apt-get update` command
task 'update_package_lists' => sub {
  exec { 'update_package_lists':
    command => 'apt-get update',
  }
}

# Define a task to run the `apt-get upgrade` command
task 'upgrade_packages' => sub {
  exec { 'upgrade_packages':
    command => 'apt-get upgrade -y',
    require => Task['update_package_lists'],
  }
}

# Define a task to check for vulnerabilities using the `apt-get --only-upgrade --no-install-recommends dist-upgrade` command
task 'check_vulnerabilities' => sub {
  exec { 'check_vulnerabilities':
    command => 'apt-get --only-upgrade --no-install-recommends dist-upgrade -s',
    require => Task['update_package_lists'],
  }
}

# Schedule the tasks to run regularly
cron { 'update_package_lists':
  command => '/usr/bin/puppet task run update_package_lists',
  user    => 'root',
  minute  => [0,30],
}

cron { 'upgrade_packages':
  command => '/usr/bin/puppet task run upgrade_packages',
  user    => 'root',
  minute  => [0,30],
  require => Task['update_package_lists'],
}

cron { 'check_vulnerabilities':
  command => '/usr/bin/puppet task run check_vulnerabilities',
  user    => 'root',
  minute  => [0,30],
  require => Task['update_package_lists'],
}
```
This script defines three tasks: update_package_lists, upgrade_packages, and check_vulnerabilities. The update_package_lists task runs the apt-get update command to update the package lists. The upgrade_packages task runs the apt-get upgrade command to upgrade the packages to their latest version. The check_vulnerabilities task runs the apt-get --only-upgrade --no-install-recommends dist-upgrade -s command to check for vulnerabilities.

Additionally, the script schedules these tasks to run regularly using the cron resource. It schedules the update_package_lists task to run every 30 minutes, the upgrade_packages task to run every 30 minutes and check_vulnerabilities to run every 30 minutes.

It's important to note that this script is an example and it may not work as is. The exact commands and options used to check for vulnerabilities may vary depending on the Linux distribution you are using.

## 5 interview questions on puppet. Give answers with code examples

## How would you configure a Puppet module to install and configure a specific package on a Linux system?


```bash
# Example of a Puppet module to install and configure the Apache web server
class apache {
  package { 'httpd':
    ensure => installed,
  }

  service { 'httpd':
    ensure => running,
    enable => true,
  }

  file { '/etc/httpd/conf/httpd.conf':
    ensure  => file,
    source  => 'puppet:///modules/apache/httpd.conf',
    require => Package['httpd'],
  }
}
```

This module uses the package resource to ensure that the Apache web server package (httpd) is installed. It uses the service resource to ensure that the Apache service is running and enabled to start on boot. It also uses the file resource to copy the Apache configuration file (httpd.conf) from the Puppet server to the client and ensure that it is the correct file.

## How would you configure a Puppet class to manage a service's state and ensure that it is running on a specific port?

```bash
class myservice {
  package { 'myservice':
    ensure => installed,
  }

  service { 'myservice':
    ensure => running,
    enable => true,
  }

  file { '/etc/myservice/myservice.conf':
    ensure  => file,
    source  => 'puppet:///modules/myservice/myservice.conf',
    require => Package['myservice'],
  }
  
  firewall { '100 allow myservice':
    dport   => '1234',
    proto   => tcp,
    action  => accept,
  }
}
```

This class uses the package resource to ensure that the myservice package is installed, and the service resource to ensure that the myservice service is running and enabled. It also uses the file resource to copy the myservice configuration file from the Puppet server to the client and ensure that it is the correct file. Additionally, it uses the firewall resource to open port 1234 on the firewall to allow traffic to the service.

## How would you use Puppet to manage a user's home directory and ensure that specific files and directories exist within it?

```bash
user { 'myuser':
  ensure     => present,
  home       => '/home/myuser',
  managehome => true,
}

file { '/home/myuser/importantfile':
  ensure  => file,
  source  => 'puppet:///modules/myuser/importantfile',
  owner   => 'myuser',
  group   => 'myuser',
  mode    => '0600',
}

file { '/home/myuser/project':
  ensure => directory,
  owner   => 'myuser',
  group   => 'myuser',
  mode    => '0700',
  recurse => true,
}
```

This code uses the user resource to create a user named 'myuser' if it does not exist, and set its home directory to '/home/myuser' and managehome to true. It uses the file resource to ensure that the file '/home/myuser/importantfile' is present and with the correct ownership, group and permissions. It also uses the file resource to create a directory named '/home/myuser/project' and set the correct ownership, group and permissions, also recursing all subdirectories.

## How would you use Puppet to manage a service's configuration file and ensure that specific values are set within it?
```bash
class myservice {
  package { 'myservice':
    ensure => installed,
  }

  service { 'myservice':
    ensure => running,
    enable => true,
  }

  file { '/etc/myservice/myservice.conf':
    ensure  => file,
    source  => 'puppet:///modules/myservice/myservice.conf',
    require => Package['myservice'],
  }

  # Use the 'augeas' resource to set specific values in the configuration file
  augeas { 'myservice_config':
    context  => '/files/etc/myservice/myservice.conf',
    changes  => [
      "set log_level info",
      "set listen_address 0.0.0.0",
    ],
    require  => File['/etc/myservice/myservice.conf'],
    notify   => Service['myservice'],
  }
}
```

This class uses the augeas resource to modify the values of specific keys in the myservice configuration file. It modifies the log_level to be set to "info" and the listen_address to "0.0.0.0", and requires the configuration file resource to be executed before it and notify the service resource to restart the service.

## How would you use Puppet to manage a cron job and ensure that it runs at a specific time and with specific command?
```bash
cron { 'mycronjob':
  ensure    => present,
  command   => '/usr/local/bin/mycommand arg1 arg2',
  user      => 'myuser',
  minute    => '0',
  hour      => '2',
  monthday  => '*',
  month     => '*',
  weekday   => '*',
}
```

This code uses the cron resource to create a cron job named 'mycronjob' if it does not exist, and set it to run the command '/usr/local/bin/mycommand arg1 arg2' at 2 AM every day, as the user 'myuser'.


