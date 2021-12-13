## General Changes

- use Django URL Validator (line 159)
- internal and external URLs separate (line 126)
- add thread_id in crawl (line 74)
- Support Multithreading

https://try.powermapper.com/Demo/Report/11bd6312-bab9-47ad-8cca-5a4dda567111

Homepage
	- checkbox to honor robots.txt
	- URL textfield
	- Analyze Button
	- Results from last scan link (ViewScanCookie)
	
Dashboard
	- Crawl Summary
	- Issues
	- Pages
		- Pages With Errors
		- Type [Document(pdf, HTML, docx), Images(gif, png, jpeg, svg), Misc(css, js, Fonts, Data, other), Links (Special - robots.txt, ads.txt)]
		- Excluded Pages
	
Analyze
	- Errors
		- SSL Check
		- Load Times
	- Accessibility
		- WCAG (https://www.w3.org/TR/WCAG-TECHS/H71.html)
		- HTML5 (https://html.spec.whatwg.org/multipage/)
		- ARIA (https://www.w3.org/TR/html-aria/#el-input-checkbox)
	- Compatibility (IE	Edge	Firefox	Safari	Opera	Chrome	iOS	Android) Mobile
		- Internet Explorer CSS rgba() colors with 3 values are not supported in all browsers. (https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)
		- IE The CSS star filter no longer works in IE7 or later. (https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/)
	- Search (Google, BING, Yahoo, Robots.txt, Search Best Practices)
		- This page has more than one h1 element, which violates Bing webmaster guidelines. (https://www.bing.com/webmaster/help/webmaster-guidelines-30fba23a)
		- This page has no h1 element, which violates Bing webmaster guidelines.
	- Standard (W3C HTML/XHTML Validation, W3C CSS Validation, W3C Deprecated Features, WHATWG)
		- Attribute :ga-event-category not allowed on element.
		- Attribute :src not allowed on element.
		- Duplicate attribute id.	
	- Usability (Usability.gov Guidelines, W3C Best Practices, Readibility)
		- Have a link labeled 'Home' on every page on the site, except for the home page. (https://www.powermapper.com/products/sortsite/rules/usegov5.1/)
		- Users should be able to quickly look at each link and tell where it goes.
		- Avoid underlined text - people will click on it and think it's a broken link.
		- Keep URLs shorter than 78 characters so they don't wrap when emailed. (https://www.w3.org/TR/2003/NOTE-chips-20030128/#gl1)
		- Omitting img width or height attributes makes the page layout jump about as images load.
	
Utils
	- get_time
	- get_full_time
	- is_valid_url
	- 
	
	
Future Features:
	- Parameters to Crawl (Some URL parameters can change page content. Which parameters should the spider pay attention to when crawling?)
	- Directories and URL to exclude (Excluding pages can reduce the load on the crawler and keep you from reaching the URL cap so you can analyze more of your sites. Enter the full path, or a substring of the URLs you wish to exclude.)
	- Results from last scan link (ViewScanCookie)
	
	
	
[Priority 1]
A Web content developer must satisfy this checkpoint. Otherwise, one or more groups will find it impossible to access information in the document. Satisfying this checkpoint is a basic requirement for some groups to be able to use Web documents.
[Priority 2]
A Web content developer should satisfy this checkpoint. Otherwise, one or more groups will find it difficult to access information in the document. Satisfying this checkpoint will remove significant barriers to accessing Web documents.
[Priority 3]
A Web content developer may address this checkpoint. Otherwise, one or more groups will find it somewhat difficult to access information in the document. Satisfying this checkpoint will improve access to Web documents.


Conformance Level "A": all Priority 1 checkpoints are satisfied;
Conformance Level "Double-A": all Priority 1 and 2 checkpoints are satisfied;
Conformance Level "Triple-A": all Priority 1, 2, and 3 checkpoints are satisfied;


Github check Links:
https://github.com/dmpayton/webalin/blob/master/webalin.py
https://github.com/brailcom/wachecker/blob/29633fd5f0f1fe58ab9c4f22bdeebcc73333d6ae/tests/standard.py



Easy Checks which can be implemented:
https://www.w3.org/TR/WCAG20-TECHS/H94.html
https://www.w3.org/TR/WCAG20-TECHS/H57.html
https://www.w3.org/TR/WCAG20-TECHS/H74.html


Compliance Models:
ARIA
WCAG 2.0
Section 508 of the Rehabilitation Act - 82 FR 5790 (2017)
W3C Usability Best Practices
Usability.gov: Research-Based Web Design & Usability Guidelines	
HTML5


Github Ref for future:
https://blog.devgenius.io/creating-an-efficient-web-crawler-in-go-e4eec36bbf8c
https://github.com/shubham-MLwiz/Advanced-Web-Crawler/blob/master/crawler.py
https://github.com/sangaline/advanced-web-scraping-tutorial
http://www.cs.uccs.edu/~jkalita/work/StudentResearch/PatwaMSProject2006.pdf
https://www.screamingfrog.co.uk/seo-spider/
https://raptor-dmt.com/tools/web-crawler-features/


IMP - https://try.powermapper.com/demo/Report/7a74be65-6caf-450f-83a9-5f8c928ad242
https://github.com/rivermont/spidy/blob/master/spidy/crawler.py




captcha - 2Captcha, Death by Captcha, and Bypass Captcha.



Getting time 
Logging info/errors/events/warnings


Faster Crawling:
Eventlet for faster multiple requests
Multi THreading - https://stackoverflow.com/questions/2632520/what-is-the-fastest-way-to-send-100-000-http-requests-in-python
