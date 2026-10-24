with open('services.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace Phase 02 container id
c = c.replace(
    '<div id="creative" class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">\n      <div class="container mx-auto">\n        <!-- Dept Header -->\n        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">\n            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: \'Sora\', sans-serif; letter-spacing: 1px; text-transform: uppercase;">\n              Phase 02',
    '<div id="development" class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">\n      <div class="container mx-auto">\n        <!-- Dept Header -->\n        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">\n            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: \'Sora\', sans-serif; letter-spacing: 1px; text-transform: uppercase;">\n              Phase 02'
)

# Replace Phase 03 container id
c = c.replace(
    '<div id="creative" class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">\n      <div class="container mx-auto">\n        <!-- Dept Header -->\n        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">\n            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: \'Sora\', sans-serif; letter-spacing: 1px; text-transform: uppercase;">\n              Phase 03',
    '<div id="marketing" class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">\n      <div class="container mx-auto">\n        <!-- Dept Header -->\n        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">\n            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: \'Sora\', sans-serif; letter-spacing: 1px; text-transform: uppercase;">\n              Phase 03'
)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated phase IDs in services.html')
