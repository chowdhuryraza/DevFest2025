# DevFest2025

<samp>
<p>
Millions of elderly people and immigrants struggle with medication due to language barriers and forgetfulness.  
While doctors and pharmacies may send reminders, they often can't communicate in the patient's native language or dialect,  
leading to misunderstandings and missed doses.
</p>

<p>
CareLingo bridges this gap by providing a smart, automated reminder system that ensures patients never miss their medication -- done all in their own language!
</p>

<h2>Key Features</h2>

- <b>Guardian-Powered Reminders</b> – Family members can register as guardians to schedule medication alerts for loved ones  
- <b>Real-Time Voice Calls</b> – We utilize the Twilio API to deliver medication reminders via automated voice calls  
- <b>Multi-Language Support</b> – Powered by Google Translate, our system speaks in the patient's native language  
- <b>Custom Schedules</b> – Users can set reminders for specific hours and days based on each patient's needs  

<h2>Our Tech Stack</h2>

- <b>Python (Flask)</b>: API and backend logic
- <b>MongoDB</b>: NoSQL database for storing prescription and recipient data
- <b>Twilio</b>: Automated voice calls for reminders
  
- <b>React</b>: User interface
- <b>TypeScript</b>: Type-safe frontend development

<h2>Design</h2>

<p>
Each guardian can register multiple patients, each with their own prescriptions.  
Prescriptions include specific days and times for automated medication reminders.  
</p>

<p>
A scheduled cron job continuously scans our database for upcoming reminders.  
When it's time, we trigger a Twilio API call, converting text to speech using Google Translate  
to ensure the patient receives the reminder in their preferred language.
</p>

<h2>Future Work</h2>

- Expand time options to support biweekly and monthly reminders  
- Allow patients to receive reminders via SMS in addition to voice calls  
- Connect with healthcare providers for direct prescription updates 

</samp>
