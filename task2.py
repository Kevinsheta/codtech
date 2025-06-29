import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Step 1: Read data
df = pd.read_csv("data.csv")

# Step 2: Basic Analysis
average_score = df['Score'].mean()
topper = df.loc[df['Score'].idxmax()]

# Step 3: Generate PDF
pdf_file = "report.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 20)
c.drawString(50, height - 50, "Automated Report")

# Add summary
c.setFont("Helvetica", 12)
c.drawString(50, height - 100, f"Total Students: {len(df)}")
c.drawString(50, height - 120, f"Average Score: {average_score:.2f}")
c.drawString(50, height - 140, f"Topper: {topper['Name']} with Score {topper['Score']}")

# Add table headers
c.drawString(50, height - 180, "Name")
c.drawString(200, height - 180, "Score")

# Add table content
y = height - 200
for index, row in df.iterrows():
    c.drawString(50, y, str(row['Name']))
    c.drawString(200, y, str(row['Score']))
    y -= 20

# Save PDF
c.save()
print("PDF report generated successfully!")
