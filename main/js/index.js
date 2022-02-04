

function signIn() {
    var {PythonShell} = require('python-shell');
    var path = require("path")
    
    console.log(
        'yeah'
    )
    var username = document.getElementById("username").value
    document.getElementById("username").value = ""

    var password = document.getElementById("passw").value
    document.getElementById("passw").value = ""

    var options = {
        scriptPath : path.join(__dirname, '../python/API/signin'),
        pythonPath: '/usr/bin/python3',
        args: [username, password]
    }

    var signin = new PythonShell("signin.py", options);

    signin.on('message', function(message){
        // swal(message);
        console.log(message)
        if (message === 'operator'){
            window.location.assign('operator.html')
        }else if (message==='admin')
        {
            window.location.assign('admin.html')
        }


    })

    // PythonShell.run('python/API/signin/signin.py', null, function (err) {
    //     if (err) throw err;
    //     console.log('finished');
    //   });
    
  
    

    // signin.end(function(err,code,message){
        
    //     console.log(err)
    //     console.log(message)
    // })

}