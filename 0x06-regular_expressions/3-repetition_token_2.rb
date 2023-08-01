#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/hbt{1,4}n/).join
end
