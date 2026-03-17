HW1 – Gemini Model Comparison



What this script does

This script loads a Gemini API key from a .env file, sends the same prompt to two Gemini models, and prints their responses, token usage, and latency.



How to run



1) Clone the repository

2) Navigate to the hw01 folder

3) Create a `.env` file containing your API key:



GEMINI\_API\_KEY=your\_real\_key\_here



4) Install dependencies



pip install -r requirements.txt



5) Run the program



python main.py



--Models used:



\- gemini-3-flash-preview

\- gemini-3.1-flash-lite-preview



--Prompt used:



Explain in three short sentences why version control is important.



--Token and Performance Table:



Model	      |	gemini-3-flash-preview |  gemini-3.1-flash-lite-preview

Input Tokens  |	12		       |  12

Output Tokens |	47		       |  67

Total Tokens  |	434		       |  79

Latency (s)   |	3.509		       |  6.909




--Reflection:


I was surprised by how quickly the Gemini models generated responses to the prompt.  

The flash model produced a shorter explanation while the lite model generated a more detailed answer.  

The token usage was smaller than I expected for the amount of information returned.  

It was interesting to compare the latency between the two models.  

This assignment helped me understand how AI APIs can be integrated into real Python programs.

