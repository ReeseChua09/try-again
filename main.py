from pyscript import display, document

def intrams_checker(e):
    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''
    
    registration_input = document.querySelector('input[name="registration"]:checked')
    if registration_input is None:
        display("Please select if you have registered online.", target='output')
        return
    registration = registration_input.value
    
    clearance_input = document.querySelector('input[name="clearance"]:checked')
    if clearance_input is None:
        display("Please select your medical clearance status.", target='output')
        return
    clearance = clearance_input.value
    
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value
    
    if registration != 'registered':
        display('Whoops! Looks like you did not register! Ask your PE teacher regarding the online registration.', target='output')
    elif clearance != 'cleared':
        display('Oh no! You need a medical clearance to join. Go to your campus clinic and secure your clearance.', target='output')
    elif section == 'emerald':
        display("LET'S GO BLUE BEARS !!!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/blue_bears.jpg" alt="Blue Bears" style="max-width:200px;">'
    elif section == 'ruby':
        display("BOOM! GO RED BULLDOGS!!!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/red_bulldogs.jpg" alt="Red Bulldogs" style="max-width:200px;">'
    elif section == 'sapphire':
        display("RISE UP! YELLOW TIGERS!!!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/yellow_tigers.jpg" alt="Yellow Tigers" style="max-width:200px;">'
    else:
        display("FIGHT STRONG! GO GREEN HORNETS!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/green_hornets.jpg" alt="Green Hornets" style="max-width:200px;">'
