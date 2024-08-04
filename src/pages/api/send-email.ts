import type { APIRoute } from 'astro';
import nodemailer from 'nodemailer';
export const POST: APIRoute = async ({ request }) => {
console.log('Received POST request to /api/send-email');
const formData = await request.formData();
const name = formData.get('name') as string;
const email = formData.get('email') as string;
const subject = formData.get('subject') as string;
const message = formData.get('message') as string;
console.log('Form data:', { name, email, subject, message });
if (!import.meta.env.SENDGRID_API_KEY) {
console.error('SENDGRID_API_KEY is not set');
return new Response(JSON.stringify({ message: 'Server configuration error' }), {
status: 500,
headers: { 'Content-Type': 'application/json' }
});
}
const transporter = nodemailer.createTransport({
host: 'smtp.sendgrid.net',
port: 587,
secure: false,
auth: {
user: 'apikey',
pass: import.meta.env.SENDGRID_API_KEY
}
});
try {
console.log('Attempting to send email');
await transporter.sendMail({
from: '"DigitalFusion Kontaktní Formulář" noreply@digitalfusion.cz',
to: 'info@digitalfusion.cz',
subject: Nová zpráva: ${subject},
text:         Jméno: ${name}         Email: ${email}         Předmět: ${subject}         Zpráva:         ${message}      ,
html:         <h2>Nová zpráva z kontaktního formuláře</h2>         <p><strong>Jméno:</strong> ${name}</p>         <p><strong>Email:</strong> ${email}</p>         <p><strong>Předmět:</strong> ${subject}</p>         <p><strong>Zpráva:</strong></p>         <p>${message}</p>      
});
console.log('Email sent successfully');
Copyreturn new Response(JSON.stringify({ message: 'E-mail byl úspěšně odeslán' }), {
  status: 200,
  headers: { 'Content-Type': 'application/json' }
});
} catch (error) {
console.error('Error sending email:', error);
return new Response(JSON.stringify({ message: 'Při odesílání e-mailu došlo k chybě', error: error.message }), {
status: 500,
headers: { 'Content-Type': 'application/json' }
});
}
};