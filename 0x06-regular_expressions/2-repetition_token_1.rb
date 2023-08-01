#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/hb{0,1}tn/).join
end
