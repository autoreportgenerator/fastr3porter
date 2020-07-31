#Auto bug bounty report generator by Nebulaex(Bounty Hunter)
#With Markdown Langauge
#bugcrowd.com/nebulaex (My bugcrowd profile)






print("""
This tool is designed for bug bounty hunters..
Developers:
	
------------------------------------------------------- 
Hello, please select a number to choose a vulnerability 
1 - SQL Injection (If you need just poc write "1poc")
2 - Open Redirect (No support just poc)
3 - Information Disclosure (No support just poc)
4 - Xss (Cross site scripting)

Other vulnerabilities coming soon

 """)
vulnerability = input("(Q) - Select Vulnerability: " )
print("\n")
if vulnerability == "1":
	bug_url = input("(Q) - Vulnerable URL: ")
	print("\n")
	sql_type = input("(Q) - SQL Injection Type(Exmpl:Boolean Based Blind SQL) :  ")
	print("\n")
	parameter = input("(Q) - Vulnerable Parameter or End-point: ")
	print("\n")
	Poc = input("(Q) - Database information(For PoC): ")
	print("\n")
	database_type = input("(Q) - Type Of Database(Example: MySQL,PostgreSQL,SQL Server .....):  ")
	print("\n")
	payload = input("(Q) - What is your payload for exploit the sql injection")
	print("\n")
	extra_information = input("""(Q) - Will you write "Description" text(As manual)? [Y/n] :  """)
	print("\n")
	if extra_information == "y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "
		
	if extra_information == "Y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "	
	if extra_information == "":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "	
	elif extra_information == "n":
		description2 = ""
		no_desc = """
*No Description*	
		"""
	elif extra_information == "N":
		description2 = ""
		no_desc = """
*No Description*	
		"""				



	print("Your report generated!!!")
	print("\n")
	print(no_desc)
	print(f"Title: {sql_type} at {parameter}")
	
	print(f"""

#Summary

While discovering your website I came across {sql_type}.

Vulnerable url = {bug_url}

#PoC (Proof Of Concept)

I managed to extract the names of {database_type} database with sql injection.
Database information ==>

```
{Poc}
```
{description2}
""")
	print("""
#Mitigation

Sanitize user input and use stored procedures.

#Impact

An attacker could access the Database and harvest potentially sensitive data from the website or even take over the entire website through using certain SQL commands.	
	
	""")

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

if vulnerability == "1poc":
	database_type = input("(Q) - Type Of Database(Example: MySQL,PostgreSQL,SQL Server .....):  ")
	parameter = input("(Q) - Vulnerable Parameter or End-point: ")
	poc = input("(Q) - Database information(For PoC): ")
	print(f"Title: {parameter}")
	print(f"""

#PoC (Proof Of Concept)

I managed to extract the names of {database_type} database with sql injection.
Database Information ==>

```
{poc}
```
""")

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

if vulnerability == "2":
	bug_url = input("(Q) - Vulnerable URL: ")
	print("\n")
	parameter = input("(Q) - Vulnerable Parameter: ")
	print("\n")
	extra_information = input("""(Q) - Will you write "Description" text(As manual)? [Y/n] :  """)
	print("\n")
	if extra_information == "y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "
	if extra_information == "":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "			
	if extra_information == "Y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "	

	elif extra_information == "n":
		description2 = ""
		no_desc = """
*No Description*	
		"""
	elif extra_information == "N":
		description2 = ""
		no_desc = """
*No Description*	
		"""				



	print("Your report generated!!!")
	print("\n")
	print(no_desc)
	print(f"Title: Open Redirect via {parameter} parameter")
	
	print(f"""

#Summary

While discovering your website I came across open redirect vulnerability.

Vulnerable url = {bug_url}

#PoC (Proof Of Concept)

Click this link and see the redirect!

```
{bug_url}
```
{description2}
""")
	print("""

#Impact

User can be redirect to malicious site.
About Open Redirect Vulnerabilities ---> `https://cwe.mitre.org/data/definitions/601.html`
	""")

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

if vulnerability == "3":
	bug_url = input("(Q) - Vulnerable URL: ")
	print("\n")
	parameter = input("(Q) - What does this url reveal?(php,user,system version...): ")
	print("\n")
	extra_information = input("""(Q) - Will you write "Description" text(As manual)? [Y/n] :  """)
	print("\n")
	if extra_information == "y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "
		
	if extra_information == "Y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "	
	if extra_information == "":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "			
	elif extra_information == "n":
		description2 = ""
		no_desc = """
*No Description*	
		"""
	elif extra_information == "N":
		description2 = ""
		no_desc = """
*No Description*	
		"""				



	print("Your report generated!!!")
	print("\n")
	print(no_desc)
	print(f"Title: Information Disclosure at {bug_url}")
	
	print(f"""

#Summary

While discovering your website I came across a information leak.

Vulnerable url = {bug_url}

#PoC (Proof Of Concept)

This link gives you {parameter} information.
Click this link and see..

```
{bug_url}
```
{description2}
""")
	print("""

#Impact

Attackers can use this information to carry out various attacks.
	""")	

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

if vulnerability == "4":
	bug_url = input("(Q) - Vulnerable URL: ")
	print("\n")
	parameter = input("(Q) - What is type of XSS? (Self,stored,reflected...)?: ")
	print("\n")
	code_part = input("(Q) - A piece of code where javascript code is run: ")
	print("\n")
	payload = input("(Q) - What is your valid payload for alert-box?: ")
	print("\n")
	extra_information = input("""(Q) - Will you write "Description" text(As manual)? [Y/n] :  """)
	print("\n")
	if extra_information == "y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "
	if extra_information == "":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "	
	
	if extra_information == "Y":
		description1 = input("(Q) - Write your Description: ")
		description2 = f"""
#Description

{description1}

		"""
		no_desc = " "	

	elif extra_information == "n":
		description2 = ""
		no_desc = """
*No Description*	
		"""
	elif extra_information == "N":
		description2 = ""
		no_desc = """
*No Description*	
		"""				



	print("Your report generated!!!")
	print("\n")
	print(no_desc)
	print(f"Title: {parameter} XSS at {bug_url}")
	
	print(f"""

#Summary

While discovering your website I came across a {parameter} xss.

Vulnerable url = {bug_url}

#PoC (Proof Of Concept)

Vulnerable code part
```
{code_part}
```
My Payload 
```
{payload}
```
{description2}
""")
	print(f"""

#Impact

Attackers can use javascript code as {parameter} 
	""")	



