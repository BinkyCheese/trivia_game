import random

# All 100 trivia questions (stored as dictionaries with question, options, and answer)
questions = [
    # Set 1
    {"question": "What British inventor is credited for developing the concept of the world's first programmable computer, the Analytical Engine, in the 1830s?",
     "options": ["A. Alan Turing", "B. Ada Lovelace", "C. Charles Babbage", "D. John von Neumann"], "answer": "C"},
    {"question": "Who invented the first mass-produced, practical sewing machine in 1846, revolutionizing the textile industry?",
     "options": ["A. Isaac Singer", "B. Elias Howe", "C. Walter Hunt", "D. Barthélemy Thimonnier"], "answer": "B"},
    {"question": "What French chemist and microbiologist is credited with a namesake discovery that revolutionized food preservation?",
     "options": ["A. Louis Pasteur", "B. Alexander Fleming", "C. Marie Curie", "D. Antoine Lavoisier"], "answer": "A"},
    {"question": "Known for her pioneering research on radioactivity, who was the first woman to win a Nobel Prize?",
     "options": ["A. Stephanie Kwolek", "B. Rosalind Franklin", "C. Marie Curie", "D. Ada Lovelace"], "answer": "C"},
    {"question": "What Austrian neurologist is credited with inventing psychoanalysis, a clinical method for treating psychopathology through dialogue between a patient and a psychoanalyst?",
     "options": ["A. Alfred Adler", "B. Carl Jung", "C. Wilhelm Reich", "D. Sigmund Freud"], "answer": "D"},
    {"question": "Name the company that introduced the first commercially available lithium-ion battery in 1991.",
     "options": ["A. Panasonic", "B. Sony", "C. Duracell", "D. Energizer"], "answer": "B"},
    {"question": "What is the name of the French physicist who invented the electric battery and discovered several elements, including sodium and potassium?",
     "options": ["A. Joseph-Louis Lagrange", "B. Jacques Charles", "C. Antoine Lavoisier", "D. André-Marie Ampère"], "answer": "C"},
    {"question": "In what year was the World Wide Web invented, revolutionizing the way information is shared on the internet?",
     "options": ["A. 1979", "B. 1984", "C. 1989", "D. 1991"], "answer": "C"},
    {"question": "What scientist developed the first successful polio vaccine in the 1950s?",
     "options": ["A. Jonas Salk", "B. Albert Sabin", "C. Edward Jenner", "D. Alexander Fleming"], "answer": "A"},
    {"question": "What is the name of the scientist credited with the discovery of penicillin in 1928?",
     "options": ["A. Alexander Fleming", "B. Louis Pasteur", "C. Marie Curie", "D. Antoine Lavoisier"], "answer": "A"},
    # Set 2
    {"question": "In the song 'Stairway to Heaven,' what mystical object is mentioned that is said to be bought with a 'bustle in your hedgerow'?",
     "options": ["A. May Queen", "B. Crystal Ball", "C. Magic Wand", "D. Enchanted Mirror"], "answer": "A"},
    {"question": "In the song 'Born to Run' by Bruce Springsteen, what is the name of the main character's partner who says 'I wanna die with you, Wendy, on the street tonight'?",
     "options": ["A. Mary", "B. Jenny", "C. Wendy", "D. Sarah"], "answer": "C"},
    {"question": "What is the real name of the guitarist known as Slash, famous for his work with Guns N' Roses?",
     "options": ["A. Saul Hudson", "B. Angus Young", "C. David Howell Evans", "D. Steve Hackett"], "answer": "A"},
    {"question": "Which iconic musician is better known by the stage name 'Meat Loaf'?",
     "options": ["A. David Coverdale", "B. Michael Lee Aday", "C. Bruce Dickinson", "D. Paul Rodgers"], "answer": "B"},
    {"question": "In what year did Jimi Hendrix pass away at the age of 27?",
     "options": ["A. 1967", "B. 1969", "C. 1970", "D. 1971"], "answer": "C"},
    {"question": "Which legendary guitarist, known for his work with the bands Cream and The Yardbirds, was famously referred to as the 'Godfather of Rock Guitar'?",
     "options": ["A. Eric Clapton", "B. Jimmy Page", "C. Jimi Hendrix", "D. Jeff Beck"], "answer": "A"},
    {"question": "In which year did The Beatles release their iconic album 'Sgt. Pepper's Lonely Hearts Club Band'?",
     "options": ["A. 1965", "B. 1966", "C. 1967", "D. 1968"], "answer": "C"},
    {"question": "Who was the lead vocalist of the band Led Zeppelin, known for his powerful voice and charismatic stage presence?",
     "options": ["A. Roger Daltrey", "B. Freddie Mercury", "C. Mick Jagger", "D. Robert Plant"], "answer": "D"},
    {"question": "What is the title of the debut studio album by the American rock band Nirvana, released in 1989?",
     "options": ["A. In Utero", "B. Nevermind", "C. Bleach", "D. Rarities"], "answer": "C"},
    {"question": "What is the name of the lead guitarist of the band Queen, known for his unique playing style and flamboyant stage persona?",
     "options": ["A. Eddie Van Halen", "B. Brian May", "C. Jimmy Page", "D. Ritchie Blackmore"], "answer": "B"},
    # Set 3
    {"question": "What is the name of the closest star to Earth, besides the Sun?",
     "options": ["A. Sirius", "B. Alpha Centauri", "C. Proxima Centauri", "D. Betelgeuse"], "answer": "C"},
    {"question": "Which planet in our solar system has the most moons?",
     "options": ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"], "answer": "A"},
    {"question": "What is the name of the largest volcano in our solar system, located on Mars?",
     "options": ["A. Mount Etna", "B. Mauna Kea", "C. Olympus Mons", "D. Mount Vesuvius"], "answer": "C"},
    {"question": "Which space mission successfully landed humans on the Moon for the first time?",
     "options": ["A. Apollo 11", "B. Mercury-Atlas 6", "C. Voyager 1", "D. Mars Pathfinder"], "answer": "A"},
    {"question": "What is the term for the point in a planet's orbit around the Sun where it is closest to the star?",
     "options": ["A. Aphelion", "B. Perihelion", "C. Equinox", "D. Solstice"], "answer": "B"},
    {"question": "What is the name of the spacecraft launched by NASA in 2006 to study Pluto and the Kuiper Belt objects?",
     "options": ["A. Galileo", "B. Juno", "C. Cassini", "D. New Horizons"], "answer": "D"},
    {"question": "In the movie 'Deep Impact,' what was the name of the meteor headed towards Earth?",
     "options": ["A. Messiah", "B. Wolf-Biederman", "C. Jensen-Bisach", "D. Smith-Johnson"], "answer": "B"},
    {"question": "What is the largest known planet outside our solar system?",
     "options": ["A. Kepler-22b", "B. WASP-17b", "C. HD 209458b", "D. TrES-4"], "answer": "B"},
    {"question": "Which spacecraft conducted the first flyby of Jupiter and Saturn, providing crucial data and images of these gas giants?",
     "options": ["A. Voyager 1", "B. Voyager 2", "C. Juno", "D. Cassini"], "answer": "A"},
    {"question": "What is the approximate age of the universe, according to current scientific estimates?",
     "options": ["A. 4.6 billion years", "B. 13.8 billion years", "C. 20 billion years", "D. 100 billion years"], "answer": "B"},
    # Set 4
    {"question": "Who was the notorious American financier convicted of running a Ponzi scheme considered the largest financial fraud in U.S. history?",
     "options": ["A. Bernie Madoff", "B. Jordan Belfort", "C. Kenneth Lay", "D. Gordon Gekko"], "answer": "A"},
    {"question": "Which former chairman of Enron Corporation was convicted of multiple counts of fraud and conspiracy related to the company's collapse?",
     "options": ["A. Martha Stewart", "B. Kenneth Lay", "C. Jeffrey Skilling", "D. Bernie Ebbers"], "answer": "B"},
    {"question": "What infamous American fraudster and stock market manipulator was convicted of numerous offenses related to his investment firm, Stratton Oakmont?",
     "options": ["A. Frank Abagnale", "B. Charles Ponzi", "C. Ivan Boesky", "D. Jordan Belfort"], "answer": "D"},
    {"question": "Who was the mastermind behind the largest insider trading scandal in U.S. history, involving illegal activities at the hedge fund SAC Capital Advisors?",
     "options": ["A. Michael Milken", "B. Bernard Madoff", "C. Raj Rajaratnam", "D. Steven Cohen"], "answer": "D"},
    {"question": "Which American businesswoman was convicted of conspiracy, fraud, and obstruction of justice related to the collapse of her company, Theranos?",
     "options": ["A. Elizabeth Holmes", "B. Martha Stewart", "C. Sherron Watkins", "D. Leona Helmsley"], "answer": "A"},
    {"question": "What former CEO of WorldCom was convicted of orchestrating one of the largest accounting frauds in U.S. history, resulting in the company's bankruptcy?",
     "options": ["A. Richard Scrushy", "B. Bernard Ebbers", "C. Jeff Skilling", "D. Andrew Fastow"], "answer": "B"},
    {"question": "Who was the American businesswoman convicted of multiple charges related to the collapse of her energy trading company, Enron Corporation?",
     "options": ["A. Michelle Malkin", "B. Elizabeth Holmes", "C. Martha Stewart", "D. Rebecca Mark"], "answer": "D"},
    {"question": "Who was the American con artist who posed as an airline pilot, doctor, and lawyer, among other professions, in the 1960s and 1970s, inspiring the movie 'Catch Me If You Can'?",
     "options": ["A. Gregor MacGregor", "B. Victor Lustig", "C. Frank Abagnale", "D. Carlos Kaiser"], "answer": "C"},
    {"question": "What American mobster, known as 'Scarface,' was the leader of the Chicago Outfit during the Prohibition era and was eventually convicted of tax evasion in 1931?",
     "options": ["A. John Gotti", "B. Lucky Luciano", "C. Bugsy Siegel", "D. Al Capone"], "answer": "D"},
    {"question": "In 1971, a group of thieves tunneled into the headquarters of the Lloyds Bank in London's Marylebone district and stole valuables worth millions of pounds. What was the nickname given to this notorious heist?",
     "options": ["A. The Hatton Garden Heist", "B. The Baker Street Robbery", "C. The Lufthansa Heist", "D. The Brink's-Mat Robbery"], "answer": "B"},
    # Set 5
    {"question": "Who is known as the father of modern physics, primarily for his theory of relativity?",
     "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Niels Bohr", "D. Galileo Galilei"], "answer": "B"},
    {"question": "What physicist is famous for his law of motion and the law of universal gravitation?",
     "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Max Planck", "D. Galileo Galilei"], "answer": "B"},
    {"question": "Which scientist developed the first successful theory of evolution by natural selection?",
     "options": ["A. Charles Darwin", "B. Gregor Mendel", "C. Alfred Russel Wallace", "D. Louis Pasteur"], "answer": "A"},
    {"question": "Which chemist is credited with the discovery of the periodic table?",
     "options": ["A. Dmitri Mendeleev", "B. Antoine Lavoisier", "C. Marie Curie", "D. John Dalton"], "answer": "A"},
    {"question": "In what year did Albert Einstein win the Nobel Prize in Physics for his work on the photoelectric effect?",
     "options": ["A. 1915", "B. 1921", "C. 1933", "D. 1945"], "answer": "B"},
    {"question": "What was the name of the theory proposed by Einstein that describes the behavior of objects moving near the speed of light?",
     "options": ["A. General Relativity", "B. Special Relativity", "C. Quantum Theory", "D. Electromagnetic Theory"], "answer": "B"},
    {"question": "Who formulated the uncertainty principle, a fundamental concept of quantum mechanics?",
     "options": ["A. Niels Bohr", "B. Werner Heisenberg", "C. Max Born", "D. Albert Einstein"], "answer": "B"},
    {"question": "Which mathematician and philosopher is known for his work in geometry and his 'Elements' work, one of the most influential works in the history of mathematics?",
     "options": ["A. Euclid", "B. Archimedes", "C. Pythagoras", "D. Aristotle"], "answer": "A"},
    {"question": "What is the name of the scientist who is credited with the discovery of the electron?",
     "options": ["A. Marie Curie", "B. Ernest Rutherford", "C. J.J. Thomson", "D. Albert Einstein"], "answer": "C"},
    {"question": "What scientist is most famous for his work on the theory of electromagnetism and his equations of electricity and magnetism?",
     "options": ["A. James Clerk Maxwell", "B. Nikola Tesla", "C. Michael Faraday", "D. Thomas Edison"], "answer": "A"},
    # Set 6
    {"question": "Which famous American scientist is known for his work on electricity and inventing the lightning rod?",
     "options": ["A. Nikola Tesla", "B. Thomas Edison", "C. Benjamin Franklin", "D. Alexander Graham Bell"], "answer": "C"},
    {"question": "What scientist is credited with the first successful synthesis of an artificial element?",
     "options": ["A. Marie Curie", "B. Glenn T. Seaborg", "C. Albert Einstein", "D. James Chadwick"], "answer": "B"},
    {"question": "Which scientist is known for his contributions to the study of optics and the theory of color vision?",
     "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Michael Faraday", "D. Thomas Young"], "answer": "A"},
    {"question": "What American inventor is known for developing the electric light bulb and the phonograph?",
     "options": ["A. Nikola Tesla", "B. Alexander Graham Bell", "C. Thomas Edison", "D. Benjamin Franklin"], "answer": "C"},
    {"question": "Who is the 'father of modern chemistry' for his discovery of the Law of Conservation of Mass?",
     "options": ["A. Antoine Lavoisier", "B. Dmitri Mendeleev", "C. John Dalton", "D. Marie Curie"], "answer": "A"},
    {"question": "Which famous scientist proposed the heliocentric model of the solar system, claiming the Earth orbits the Sun?",
     "options": ["A. Isaac Newton", "B. Galileo Galilei", "C. Johannes Kepler", "D. Nicolaus Copernicus"], "answer": "D"},
    {"question": "Who developed the first vaccine for smallpox, one of the most important breakthroughs in medical science?",
     "options": ["A. Louis Pasteur", "B. Edward Jenner", "C. Albert Calmette", "D. Alexander Fleming"], "answer": "B"},
    {"question": "What physicist developed the concept of the quantum theory, which revolutionized our understanding of atomic and subatomic processes?",
     "options": ["A. Niels Bohr", "B. Werner Heisenberg", "C. Albert Einstein", "D. Max Planck"], "answer": "D"},
    {"question": "What scientist is known for his development of the laws of planetary motion?",
     "options": ["A. Johannes Kepler", "B. Isaac Newton", "C. Galileo Galilei", "D. Albert Einstein"], "answer": "A"},
    # Set 7
    {"question": "Which scientist discovered the circulation of blood in the human body?",
     "options": ["A. William Harvey", "B. Andreas Vesalius", "C. Hippocrates", "D. Claude Bernard"], "answer": "A"},
    {"question": "Which biologist is credited with developing the theory of evolution by natural selection, alongside Charles Darwin?",
     "options": ["A. Gregor Mendel", "B. Alfred Russel Wallace", "C. Louis Pasteur", "D. Thomas Malthus"], "answer": "B"},
    {"question": "What Italian scientist is famous for his pioneering work in astronomy, using telescopes to observe the planets and stars?",
     "options": ["A. Galileo Galilei", "B. Albert Einstein", "C. Isaac Newton", "D. Johannes Kepler"], "answer": "A"},
    {"question": "Which chemist was awarded the Nobel Prize for discovering the structure of the benzene molecule?",
     "options": ["A. Marie Curie", "B. Linus Pauling", "C. Robert Hooke", "D. August Kekulé"], "answer": "D"},
    {"question": "What biologist is known for his pioneering work on the theory of heredity, using pea plants?",
     "options": ["A. Gregor Mendel", "B. Charles Darwin", "C. James Watson", "D. Francis Crick"], "answer": "A"},
    {"question": "Who developed the first law of motion, which states that an object in motion stays in motion unless acted upon by an outside force?",
     "options": ["A. Galileo Galilei", "B. Isaac Newton", "C. Albert Einstein", "D. Niels Bohr"], "answer": "B"},
    {"question": "Which astronomer is known for developing the theory that planets move in elliptical orbits around the sun?",
     "options": ["A. Galileo Galilei", "B. Johannes Kepler", "C. Isaac Newton", "D. Tycho Brahe"], "answer": "B"},
    {"question": "Who was the first person to identify and name the cell, observing the structure of plant cells?",
     "options": ["A. Antonie van Leeuwenhoek", "B. Robert Hooke", "C. Louis Pasteur", "D. Albert Einstein"], "answer": "B"},
    {"question": "What scientist is best known for his discovery of the process of photosynthesis in plants?",
     "options": ["A. Antoine Lavoisier", "B. Jan Ingenhousz", "C. Albert Einstein", "D. Michael Faraday"], "answer": "B"},
    {"question": "Which scientist is credited with inventing the first successful airplane, the Wright Flyer?",
     "options": ["A. Wilbur Wright", "B. Samuel Morse", "C. Thomas Edison", "D. Alexander Graham Bell"], "answer": "A"},
    # Set 8
    {"question": "Which scientist is famous for his development of the law of electromagnetism and the concept of the electromagnetic field?",
     "options": ["A. James Clerk Maxwell", "B. Nikola Tesla", "C. Michael Faraday", "D. Albert Einstein"], "answer": "A"},
    {"question": "Who was the first woman to receive a Nobel Prize, and later became a pioneer in radioactivity?",
     "options": ["A. Marie Curie", "B. Ada Lovelace", "C. Rosalind Franklin", "D. Barbara McClintock"], "answer": "A"},
    {"question": "Who was the first African-American woman to receive a PhD in physics from MIT?",
     "options": ["A. Alice Ball", "B. Shirley Jackson", "C. Katherine Johnson", "D. Marie Maynard Daly"], "answer": "B"},
    {"question": "Which scientist discovered the structure of the DNA molecule in 1953?",
     "options": ["A. Watson and Crick", "B. Charles Darwin", "C. Isaac Newton", "D. Albert Einstein"], "answer": "A"},
    {"question": "Who developed the modern theory of plate tectonics, explaining the movement of Earth's lithosphere?",
     "options": ["A. Alfred Wegener", "B. Marie Tharp", "C. John Tuzo Wilson", "D. Carl Sagan"], "answer": "C"},
    {"question": "What physicist is known for his work on quantum mechanics and his paradox involving Schrödinger's cat?",
     "options": ["A. Albert Einstein", "B. Max Planck", "C. Werner Heisenberg", "D. Erwin Schrödinger"], "answer": "D"},
    {"question": "Which chemist is known for developing the periodic law and creating the periodic table of elements?",
     "options": ["A. Antoine Lavoisier", "B. Dmitri Mendeleev", "C. Marie Curie", "D. John Dalton"], "answer": "B"},
    {"question": "Who is known for developing the first practical telegraph and the first telephone?",
     "options": ["A. Alexander Graham Bell", "B. Nikola Tesla", "C. Samuel Morse", "D. Thomas Edison"], "answer": "A"},
    {"question": "Which scientist discovered the electron by conducting experiments with cathode rays?",
     "options": ["A. Albert Einstein", "B. Ernest Rutherford", "C. J.J. Thomson", "D. Marie Curie"], "answer": "C"},
    {"question": "What scientist invented the first modern-day vaccine for polio?",
     "options": ["A. Albert Sabin", "B. Louis Pasteur", "C. Jonas Salk", "D. Edward Jenner"], "answer": "C"},
    # Set 9
    {"question": "What famous American scientist and inventor is credited with developing the first commercially successful light bulb?",
     "options": ["A. Alexander Graham Bell", "B. Benjamin Franklin", "C. Thomas Edison", "D. Nikola Tesla"], "answer": "C"},
    {"question": "Who is the scientist behind the development of the law of gravity?",
     "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Johannes Kepler"], "answer": "B"},
    {"question": "What scientist is credited with formulating the laws of planetary motion, particularly elliptical orbits?",
     "options": ["A. Johannes Kepler", "B. Isaac Newton", "C. Galileo Galilei", "D. Tycho Brahe"], "answer": "A"},
    {"question": "Which scientist is famous for developing the theory of relativity, which changed our understanding of space and time?",
     "options": ["A. Albert Einstein", "B. Galileo Galilei", "C. Isaac Newton", "D. Niels Bohr"], "answer": "A"},
    {"question": "Who developed the first successful smallpox vaccine?",
     "options": ["A. Edward Jenner", "B. Louis Pasteur", "C. Albert Einstein", "D. John Snow"], "answer": "A"},
    {"question": "Who is known for his work on the theories of electromagnetism and the invention of the electric motor?",
     "options": ["A. Nikola Tesla", "B. James Clerk Maxwell", "C. Michael Faraday", "D. Thomas Edison"], "answer": "A"},
    {"question": "Who first theorized the existence of black holes in space?",
     "options": ["A. Albert Einstein", "B. Stephen Hawking", "C. Johannes Kepler", "D. Karl Schwarzschild"], "answer": "D"},
    {"question": "Who was the first woman to be awarded a Nobel Prize in Chemistry?",
     "options": ["A. Dorothy Crowfoot Hodgkin", "B. Marie Curie", "C. Roslyn Yalow", "D. Gerty Cori"], "answer": "B"},
    {"question": "Which scientist is famous for his work on the structure of the atom and the discovery of the neutron?",
     "options": ["A. Ernest Rutherford", "B. Niels Bohr", "C. James Chadwick", "D. Albert Einstein"], "answer": "C"},
    {"question": "What physicist developed the concept of wave-particle duality, describing the nature of light and particles?",
     "options": ["A. Albert Einstein", "B. Niels Bohr", "C. Louis de Broglie", "D. Max Planck"], "answer": "C"},
    # Set 10
    {"question": "Which biologist is credited with the discovery of the structure of the DNA molecule?",
     "options": ["A. James Watson", "B. Charles Darwin", "C. Rosalind Franklin", "D. Francis Crick"], "answer": "A"},
    {"question": "Who discovered the concept of natural selection, a key part of the theory of evolution?",
     "options": ["A. Alfred Russel Wallace", "B. Charles Darwin", "C. Gregor Mendel", "D. Isaac Newton"], "answer": "B"},
    {"question": "What physicist is known for his work on the photoelectric effect, which helped establish quantum mechanics?",
     "options": ["A. Niels Bohr", "B. Werner Heisenberg", "C. Albert Einstein", "D. Max Planck"], "answer": "C"},
    {"question": "What mathematician and physicist is best known for developing calculus alongside Isaac Newton?",
     "options": ["A. Albert Einstein", "B. Pierre-Simon Laplace", "C. Gottfried Wilhelm Leibniz", "D. Blaise Pascal"], "answer": "C"},
    {"question": "Which scientist discovered the electron?",
     "options": ["A. Albert Einstein", "B. J.J. Thomson", "C. Ernest Rutherford", "D. Louis Pasteur"], "answer": "B"},
    {"question": "Who first proposed the heliocentric theory of the solar system, stating that the Earth revolves around the Sun?",
     "options": ["A. Copernicus", "B. Galileo Galilei", "C. Johannes Kepler", "D. Isaac Newton"], "answer": "A"},
    {"question": "What scientist is known for his work on the development of the theory of electromagnetism?",
     "options": ["A. Michael Faraday", "B. Albert Einstein", "C. James Clerk Maxwell", "D. Thomas Edison"], "answer": "C"},
    {"question": "Who is known for his discoveries in the field of chemistry, including the concept of atomic structure?",
     "options": ["A. Marie Curie", "B. John Dalton", "C. Dmitri Mendeleev", "D. Robert Hooke"], "answer": "B"},
    {"question": "What American physicist is famous for his work on quantum mechanics and the uncertainty principle?",
     "options": ["A. Albert Einstein", "B. Werner Heisenberg", "C. Niels Bohr", "D. Max Planck"], "answer": "B"},
    {"question": "Who developed the first successful vaccine for polio, saving countless lives worldwide?",
     "options": ["A. Albert Sabin", "B. Jonas Salk", "C. Edward Jenner", "D. Louis Pasteur"], "answer": "B"}
]

# Function to ask questions
def ask_question(question):
    print(f"Question: {question['question']}")
    for option in question['options']:
        print(option)
    answer = input("Your answer: ").upper()
    return answer == question['answer']

# Function to play the game
def play_game():
    score = 0
    # Shuffle questions for randomness
    random.shuffle(questions)
    for question in questions[:10]:  # Limiting to 10 questions
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.\n")

    print(f"Your final score is {score}/10")

# Main game loop
def main():
    while True:
        play_game()  # Play a round of trivia
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop if user doesn't want to play again

# Run the game
if __name__ == "__main__":
    main()
