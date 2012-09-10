source "http://rubygems.org"
gem "rspec", :require => "spec" 
gem "inifile"
# To use local checkout: bundle config local.ruote-amqp /maemo/devel/BOSS/src/ruby-ruote-amqp
gem "ruote-amqp", :git => "git://github.com/MeeGoIntegration/ruote-amqp.git", :branch => "mer-v2.3.0"
gem "ruote-kit", :git => "git://github.com/MeeGoIntegration/ruote-kit.git", :branch => "mer-v2.3.0"
gem "yajl-ruby"

# That's it for our strict dependencies. However, we also want to
# ensure we're using specific git versions from things further down the tree.

# bundle config local.amqp /maemo/devel/BOSS/src/ruby-amqp
gem "amqp", :git => "git://github.com/MeeGoIntegration/amqp.git", :branch => "mer-0.9.7"
# bundle config local.ruote /maemo/devel/BOSS/src/ruby-ruote
gem "ruote", :git => "git://github.com/MeeGoIntegration/ruote.git", :branch => "mer-v2.3.0"
