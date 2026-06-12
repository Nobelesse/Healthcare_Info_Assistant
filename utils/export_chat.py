from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_chat_pdf(messages):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    for msg in messages:

        content.append(
            Paragraph(
                f"<b>{msg['role'].title()}</b>: {msg['content']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

    doc.build(content)

    buffer.seek(0)

    return buffer