#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/hbt{1,}n/).join
end
