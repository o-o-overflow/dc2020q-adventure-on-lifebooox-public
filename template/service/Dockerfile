from ubuntu:18.04

# example:
run apt-get -qq update && apt-get install -qq --no-install-recommends xinetd rsyslog
# python3-pip, etc.

# Note: anything that goes in public_files must be pre-built and checked in git
copy src/config.py /
copy service /service

run touch /flag && chmod 644 /flag && echo "OOO{this is a test flag}" > /flag


copy service.conf /service.conf
copy banner_fail /banner_fail
copy wrapper /wrapper

expose 5000
cmd ["/usr/sbin/xinetd", "-syslog", "local0", "-dontfork", "-f", "/service.conf"]
# ^^ If ps would be too revealing, replace with the line below.
#    AFAIK, this also disables the built-in printf(%n) protection, so YMMV.
#cmd chmod go-rwx /proc && /usr/sbin/xinetd -syslog local0 -dontfork -f /service.conf
