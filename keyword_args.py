# Keyword arguments example.


def generate_website(name, url="www.deitel.com",
                     Flash="no", CGI="yes"):
    print("Generating site requested by", name, "using url", url)

    if Flash == "yes":
        print("Flash is enable")

    if CGI == "yes":
        print("CGI scripts are enabled")

    print()

generate_website("Deitel")
generate_website("Deitel", Flash="yes", url="www.deitel.com/new")
generate_website(CGI="no", name="Prentice Hall")
