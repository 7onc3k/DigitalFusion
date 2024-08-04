import nodemailer from 'nodemailer';
export async function post({ request }) {
  const formData = await request.formData();
  const name = formData.get('name');
  const email = formData.get('email');
  const subject = formData.get('subject');
  const message = formData.get('message');
  const transporter = nodemailer.createTransport({
    host: 'smtp.sendgrid.net',
    port: 587,
    secure: false,
    auth: {
      user: 'apikey',
      pass: process.env.SENDGRID_API_KEY
    }
  });
  try {
    await transporter.sendMail({
      from: '"DigitalFusion Kontaktní Formulář" <noreply@digitalfusion.cz>',
      to: 'info@digitalfusion.cz',
      subject: `Nová zpráva: ${subject}`,
      text: `
        Jméno: ${name}
        Email: ${email}
        Předmět: ${subject}
        Zpráva:
        ${message}
      `,
      html: `
        <h2>Nová zpráva z kontaktního formuláře</h2>
        <p><strong>Jméno:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Předmět:</strong> ${subject}</p>
        <p><strong>Zpráva:</strong></p>
        <p>${message}</p>
      `
    });
    return new Response(JSON.stringify({ message: 'E-mail byl úspěšně odeslán' }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  } catch (error) {
    console.error('Chyba při odesílání e-mailu:', error);
    return new Response(JSON.stringify({ message: 'Při odesílání e-mailu došlo k chybě' }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
}