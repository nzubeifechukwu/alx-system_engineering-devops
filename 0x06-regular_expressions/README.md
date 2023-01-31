# Regular Expressions
## Regex
The regexp for this project are built using Oniguruma, the default regular expression library used by Ruby.

**Note:** Other regular expression libraries may have different properties.

Because the focus of this exercise is to play with regular expressions (regex), not to learn Ruby, below is the Ruby code to use (just replace the regexp part, that is the code in between the //):

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```
