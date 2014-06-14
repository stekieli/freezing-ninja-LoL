if __name__ == "__main__":
    bashCommand = "gedit frenin/models.py frenin/views.py frenin/urls.py frenin/freninhelper.py"
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
