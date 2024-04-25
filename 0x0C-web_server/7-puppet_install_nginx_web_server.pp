#!/usr/bin/env bash
# config my work using Puppet
package  { 'nginx':
  ensure => installed,
}

f
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx-enable/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite
