#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/?[0-9][0-9][0-9][ |-]?[0-9][0-9][0-9][ |-]?[0-9][0-9][0-9][0-9]/).join
end
