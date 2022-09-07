AUTHOR = "Eugene Ng"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = False
PATH = "content"
RELATIVE_URLS = True # Uncomment if you want document-relative URLs when developing
SITENAME = "Eugene Ng"
SITEURL = ""
TIMEZONE = "America/New_York"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "./pelican-resume"

# Profile information
NAME = "Eugene Ng"
TAGLINE = "Engineer"
PIC = "profile.png"

# Sidebar links
EMAIL = "eyn2@cornell.edu"
PHONE = "860 726 6143"
WEBSITE = "eugene.ng"
LINKEDIN = "eugeneyng"
GITHUB = "eugeneyng"
PDF = "https://github.com/eugeneyng/eugeneyng.github.io/content/resume.pdf"

CAREER_SUMMARY = "I am a technical project manager with 5+ years experience managing fast-paced military and commercial contracts. On the side, my company, Presque Labs LLC has won or finalized in multiple design challenges (HeroX, YCombinator). In my free time I love to stay active and play volleyball, tennis, and ski."

EDUCATIONS = [
	{
		"degree": "M. Eng, Electrical Engineering",
		"meta": "University of Connecticut",
		"time": "2018 - 2020"
	},
	{
		"degree": "M. Eng, Mechanical Engineering",
		"meta": "Cornell University",
		"time": "2016 - 2017"
	},
  {
    "degree": "B.S., Mechanical Engineering",
    "meta": "Cornell University",
    "time": "2012 - 2016"
  }
]

EXPERIENCES = [
	{
		"job_title": "Manager, Manufacturing Engineering & Operations",
		"time": "Feb 2017 - Present",
		"company": "Pratt & Whitney | Raytheon Technologies Corp",
		"details": "Oversaw procurement of hundreds of capital equipment projects totaling more than $100M per year"	
	},
	{
		"job_title": "Co-Founder",
		"time": "Jul 2015 - Present",
		"company": "Presque Labs LLC",
		"details": "Maintained and provided site reliability engineering for company website and internal applications, including Docker, Jupyter, Nginx, Nextcloud, and Wordpress"
	}
]

INTERESTS = [
	"Piano",
  "Skiing",
  "Tennis",
  "Volleyball"
]

LANGUAGES = [
	{
		"name": "English",
		"description": "Native"
	}
]

PROJECT_INTRO = ""

PROJECTS = [
	{
		"title": "Nonlinear Optimal Control of the COVID-19 Pandemic in Connecticut (2020)",
		"tagline": "Created a modified SEIR model of COVID-19 spread in Connecticut, and formulated a discrete, nonlinear, predictive, closed-loop feedback controller to minimize the number of infected. Simulated mathematical model in Python using the GEKKO optimization suite"
	},
	{
		"title": "HeroX NextGen Cart Design Challenge | Presque Labs LLC (2018)",
		"tagline": "Challenge winner for airport material transport (AMTC) concept to track and transport secured goods within an airport. Designed electrical circuit in KiCad and prototyped and fabricated PCB through OSH Park. Developed user interface and linked IoT sensors to SQL database using Python."
	},
	{
		"title": "Arachnabot, Spider-Inspired Robot | Collective Embodied Intelligence Lab (2016)",
		"tagline": "Analyzed, modeled, and simulated a to-scale jumping robot with spider-inspired joints in MATLAB, using a differential algebraic equation (DAE) method. Directed micro-fabrication using FDM and SLA 3D printing methods"
	},
  {
		"title": "Cornell Concrete Canoe (2016)",
		"tagline": "3rd place finish at 2016 ASCE Concrete Canoe Competition. Coordinated and oversaw 6 subteams (aesthetics, analysis, business, mold, mix, and paddling) and 34 persons for the 2016 ASCE Concrete Canoe Competition. Introduced novel moisture sensors and concrete curing control. Eliminated shrinkage cracking while increasing tensile and compressive strength by 62% and 35%"
	},
]

SKILLS = [
	{
    "title": "ANSYS",
    "level": "75"
  },
  {
    "title": "HTML/CSS",
    "level": "95"
  },
  {
    "title": "JavaScript",
    "level": "90"
  },
  {
    "title": "KiCad",
    "level": "75"
  },
  {
    "title": "LaTeX",
    "level": "95"
  },
  {
    "title": "MATLAB",
    "level": "95"
  },
  {
    "title": "Microsoft Access",
    "level": "95"
  },
  {
    "title": "Python",
    "level": "95"
  },
  {
    "title": "React",
    "level": "75"
  },
  {
    "title": "Solidworks",
    "level": "75"
  },
  {
    "title": "Visual Basic for Applications (VBA)",
    "level": "95"
  },
  {
    "title": "Structured Query Language (SQL)",
    "level": "90"
  },
  {
    "title": "Wordpress",
    "level": "75"
  }
]