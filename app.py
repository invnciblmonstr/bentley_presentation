import streamlit as st

st.set_page_config(
    page_title="Programming Languages You Should Know",
    page_icon="💻"
)

st.title("Programming Languages You Should Know About for Business")

def python():

    st.header("🐍 1. Python - The Charmer")
    st.markdown("""
    - Python is the enchanting snake charmer of the programming world.

    - It's easy to learn, with simple syntax and readability that make it the go-to choice for beginners.

    - Python is versatile, so you can work on anything from web development to data analysis, machine learning, and more.

    - Famous frameworks like Django, Flask, and TensorFlow make Python even more powerful.

    - Beginner's delight: Python's simplicity makes it perfect for first-time programmers.

    - Huge fan club: Python's large community means tons of libraries and support.
    """)

def intro():

    st.header("Ajinkya Deshmukh")
    col1, col2 = st.columns(2)
    col1.markdown("""
    - MSBA 2021

    - Worked at CIS Sandbox

    - From India, Currently in Texas

    - SDET at Roche (Python and Golang)

    - Parenting two pups (Niko & Layla)
    """)
    col2.image("NikoLayla.jpeg", width=300)

def java():
    st.header("☕ 2. Java - The Ageless Workhorse")
    st.markdown("""
    - Java, the evergreen stallion, has been around since the 90s but shows no signs of slowing down.

    - Its "write once, run anywhere" philosophy makes it a popular choice for cross-platform applications.

    - Java is beloved for its object-oriented programming, robust standard library, and powerful frameworks like Spring and Hibernate.

    - Whether it's Android apps, web applications, or enterprise software, Java's versatility keeps it relevant and in demand.

    - Brewing robustness: Java's strong typing and exception handling make it a robust language.
""")

def html():
    st.header("🎨3. HTML - The Web's Canvas")
    st.markdown("""
    - HTML, the painter of the web, isn't a programming language per se but a markup language that structures web content.

    - It's the backbone of every website, defining elements like headings, paragraphs, images, links, and more.

    - HTML5, the latest version, introduced new features, making the web more interactive and engaging.

    - Mastering HTML is essential for anyone interested in web development or design.
""")

def css():
    st.header("👗 4. CSS - The Web's Fashionista")
    st.markdown("""
    - CSS, the style guru, adds the pizzazz to your HTML's plain looks.

    - With CSS, you can control the layout, colors, fonts, and overall appearance of web pages.

    - It's essential for creating responsive, mobile-friendly designs that adapt to different screen sizes.

    - CSS frameworks like Bootstrap and Tailwind make it easier to create beautiful and consistent designs.
""")

def js():
    st.header("🌐 5. JavaScript - The Web Wizard")
    st.markdown("""
    - JavaScript casts its spell on the web, turning static pages into dynamic, interactive experiences.

    - It's the only programming language native to web browsers, so it's essential for front-end web development.

    - JavaScript's magic extends to back-end development, thanks to Node.js, creating full-stack wizards.

    - Async acrobatics: JavaScript excels at asynchronous programming, making it great for handling real-time data.

    - JSON joy: JavaScript Object Notation (JSON) makes data exchange between client and server simple and efficient.

    - Popular libraries and frameworks like React, Angular, and Vue.js add more sparkle to its repertoire.
""")

def go():
    st.header("🚀 2. Go (Golang) - The Speedy Guru")
    st.markdown("""
    - Go for it: Go, aka Golang, is a statically typed, compiled language developed by Google.

    - Concurrent champion: Go's built-in concurrency features make it ideal for modern, multi-core processors.

    - Simplicity and speed: Go's design emphasizes simplicity, making it easy to learn and fast to execute.

    - Cloud commander: Go is perfect for cloud computing, microservices, and containerization.

    - Garbage collector: Go's garbage collection mechanism ensures efficient memory management.

    - Networking ninja: Go is great for network programming and high-performance servers.
    
    - Goroutines galore: Go's lightweight Goroutines handle concurrent tasks efficiently and elegantly.
""")

def rust():
    st.header("🦀 7. Rust - The Fearless Protector")
    st.markdown("""
    - Rust never sleeps: Rust is a systems programming language that focuses on safety, speed, and concurrency.

    -  Memory maestro: Rust's ownership system guarantees memory safety without a garbage collector.

    - Fearless concurrency: Rust's safe concurrency features prevent race conditions and other bugs.

    - C++ challenger: Rust is an alternative to C++ for systems programming and high-performance applications.

    - WebAssembly warrior: Rust can compile to WebAssembly, making it suitable for web development.

    - Rustaceans rejoice: Rust has a friendly, growing community and excellent documentation.

    - Crate expectations: Rust's package manager, Cargo, manages dependencies and builds projects with ease.
""")

def calc():
    st.header("The Noun, Adjective, and Verb")
    co1, co2, co3 = st.columns(3)
    ht = co1.checkbox('HTML (Noun)',value= False)
    css = co2.checkbox('CSS (Adjective)',value= False)
    js = co3.checkbox('JS (Verb)',value= False)
    
    with open('script.txt','r') as fs:
         script = fs.read()
    with open('style.txt', 'r') as sf:
         style = sf.read()
    with open('body.txt', 'r') as bo:
         body = bo.read()
    head_start = """<head>\n"""
    head_end = """
    <title>Calulator</title>
</head>""" 

    if css:
         head_start += style
         
    if js:
        # final = html_string[1470:2058]
        head_start += script
    
    head_start += head_end
    if ht:
       head_start += body
    
    st.components.v1.html(head_start, width = 450,height = 470 ,scrolling=False)

def game():
    st.header("Flappy bird")
    with open('flappybird.html', 'r') as file:
        html_string = file.read()
    st.components.v1.html(html_string, width = 700,height = 400 ,scrolling=False)

def end_slide():
     st.header("Thank You")

def conclusion():
     st.markdown("""
    ### The right tool for the job: Choose the programming language that suits your project and expertise.

    - Python: Perfect for beginners, web development, data analysis, and automation tasks.
    - Java: A powerhouse for Android apps, enterprise applications, and platform-independent code.
    - HTML & CSS: The dynamic duo that makes the web beautiful and accessible.
    - JavaScript: The browser boss that brings interactivity and dynamism to web pages.
    - Go: Google's answer to modern, concurrent, and cloud-based programming.
    - Rust: A fearless, memory-safe contender for systems programming and high-performance applications.
    - SQL: The database whisperer for managing and manipulating relational databases.

    ### Keep learning: Explore new languages, frameworks, and libraries to expand your coding horizons!


""")
     
def sql():
    st.header("🧮 SQL - Query connoisseur")
    st.markdown("""
    - SQL (Structured Query Language) is the go-to language for managing relational databases.
    - CRUD-tastic: SQL allows you to Create, Read, Update, and Delete data in database tables with ease.
    - Join the party: SQL's JOIN operations enable you to retrieve data from multiple tables based on their relationships.
    - Aggregation nation: SQL's aggregate functions help you summarize and analyze large datasets (e.g., COUNT, SUM, AVG, MIN, MAX).
    - Filter frenzy: SQL's WHERE and HAVING clauses let you filter data based on specific conditions.
    - Sorting soiree: ORDER BY and GROUP BY clauses help you sort and categorize your data.
    - Database darlings: SQL is widely supported by popular databases like MySQL, PostgreSQL, SQL Server, and Oracle.
     """)

page_names_to_funcs = {
    "Intro": intro,
    "Python": python,
    "Java": java,
    "HTML": html,
    "CSS": css,
    "JavaScript": js,
    "Calculator": calc,
    "Go": go,
    "Rust": rust,
    "SQL": sql,
    "Game": game,
    "Conclusion": conclusion,
    "Thank You": end_slide
}

container = st.container()
keys = list(page_names_to_funcs.keys())

if 'count' not in st.session_state:
	st.session_state.count = 1

def increase():
	st.session_state.count += 1

def decrease():
     st.session_state.count -= 1

col1, col2, col3 = st.columns([1,5,1])

with col1:
    if st.session_state.count>=2:
        st.button('Previous', on_click=decrease)

with col2:
    st.slider("Slide",1,len(keys),st.session_state.count, disabled=True)

with col3:
    if st.session_state.count<=len(keys)-1:
        st.button('Next', on_click=increase)

with container:
        page_names_to_funcs[keys[st.session_state.count-1]]()


