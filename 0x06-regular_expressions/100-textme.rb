#!/usr/bin/env ruby
# Extracts the senders name (in from:), receiver's name (in to: ) and the
# flags in a text log
# For example, if the input is (without the comment hashtags):

# "Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS
# [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384]
# [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly
# primitive that they still think digital watches are a pretty neat idea.]"

# The output would be: 12392190384,19148265919,-1:0:-1:-1:-1

puts ARGV[0].scan(/\[from:(.+?)\].+\[to:(.+?)\].+\[flags:(.+?)\]/).join(",")
