import dns.resolver
import os
import sys

bls = ["dnsblchile.org",
"b.barracudacentral.org",
"cbl.abuseat.org",
"http.dnsbl.sorbs.net",
"misc.dnsbl.sorbs.net",
"socks.dnsbl.sorbs.net",
"web.dnsbl.sorbs.net",
"dnsbl-1.uceprotect.net",
"dnsbl-3.uceprotect.net",
"sbl.spamhaus.org",
"zen.spamhaus.org",
"hostkarma.junkemailfilter.com",
"nobl.junkemailfilter.com",
"psbl.surriel.com",
"rbl.spamlab.com",
"noptr.spamrats.com",
"dnsbl.inps.de",
"httpbl.abuse.ch",
"korea.services.net",
"wormrbl.imp.ch",
"rbl.suresupport.com",
"ips.backscatterer.org",
"multi.surbl.org",
"tor.dan.me.uk",
"access.redhawk.org",
"rbl.interserver.net",
"bogons.cymru.com",
"bl.spamcop.net",
"dnsbl.sorbs.net",
"dul.dnsbl.sorbs.net",
"smtp.dnsbl.sorbs.net",
"spam.dnsbl.sorbs.net",
"zombie.dnsbl.sorbs.net",
"dnsbl-2.uceprotect.net",
"pbl.spamhaus.org",
"xbl.spamhaus.org",
"bl.spamcannibal.org",
"ubl.unsubscore.com",
"dyna.spamrats.com",
"spam.spamrats.com",
"drone.abuse.ch",
"dul.ru",
"spamrbl.imp.ch",
"virbl.bit.nl",
"dsn.rfc-ignorant.org",
"dsn.rfc-ignorant.org",
"netblock.pedantic.org",
"ix.dnsbl.manitu.net",
"rbl.efnetrbl.org",
"dnsbl.dronebl.org",
"db.wpbl.info",
"query.senderbase.org",
"combined.rbl.msrbl.net",
"blackholes.five-ten-sg.com",
"sorbs.dnsbl.net.au",
"rmst.dnsbl.net.au",
"dnsbl.kempt.net",
"blacklist.woody.ch",
"virus.rbl.msrbl.net",
"phishing.rbl.msrbl.net",
"images.rbl.msrbl.net",
"spam.rbl.msrbl.net",
"spamlist.or.kr",
"dnsbl.abuse.ch",
"bl.deadbeef.com",
"ricn.dnsbl.net.au",
"probes.dnsbl.net.au",
"ubl.lashback.com",
"ksi.dnsbl.net.au",
"bsb.spamlookup.net",
"dob.sibl.support-intelligence.net",
"omrs.dnsbl.net.au",
"osrs.dnsbl.net.au",
"orvedb.aupads.org",
"relays.nether.net",
"relays.bl.gweep.ca",
"relays.bl.kundenserver.de",
"dialups.mail-abuse.org",
"rdts.dnsbl.net.au",
"duinv.aupads.org",
"residential.block.transip.nl",
"dynip.rothen.com",
"mail.people.it",
"blacklist.sci.kun.nl",
"spamguard.leadmon.net",
"csi.cloudmark.com"]

def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text
    return '\x1b[%dm%s\x1b[0m' % (color_code, text)

def red(text):
    return color(text, 31)

def blink(text):
    return color(text, 5)

def green(text):
    return color(text, 32)

def blue(text):
    return color(text, 34)

def yellow(text):
    return color(text, 33)

def purple(text):
    return color(text, 35)

IPs = [
"X.X.X.X"
]

for IP in IPs:
    BAD = 0
    GOOD = 0
    print 'Checking IP %s:' %(IP)

    for bl in bls:
        try:
            my_resolver = dns.resolver.Resolver(configure=False)
            query = '.'.join(reversed(str(IP).split("."))) + "." + bl
            my_resolver.timeout = 30
            my_resolver.lifetime = 30
            my_resolver.nameservers = ["8.8.8.8"]
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")
            print (yellow('IP: %s IS listed in %s (%s: %s)')) %(IP, bl, answers[0], answer_txt[0])
            BAD = BAD + 1

        except dns.resolver.NXDOMAIN:
            #print (green('IP: %s is NOT listed in %s')) %(IP, bl)
            GOOD = GOOD + 1

        except dns.resolver.Timeout:
            print (red('WARNING: %s Timeout!')) %(bl)

        except dns.resolver.NoNameservers:
            print (red('WARNING: No nameservers for %s')) %(bl)

        except dns.resolver.NoAnswer:
            print (red('WARNING: No answer for %s')) %(bl)

    print(blue('%s is on %s/%s blacklists.')) %(IP, BAD, GOOD+BAD)
