<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="style.css">
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <title>Relay v1.0</title>
</head>
<body style="background-color:#303030">
<section id="cover" class="min-vh-100">
    <div id="cover-caption">
        <div class="container">
            <div class="row text-white">
                <div class="col-md-4 col-md-offset-4 col-xs-6 col-xs-offset-3 mx-auto text-center form p-4">
                    <h1 class="display-4 py-1 text-truncate text-primary">Relay<h1>
                    <div class="px-2">
                        <form action="../../cgi-bin/client.py" method="post" class="justify-content-center">
                            <div class="form-group">
                                <label class="sr-only">Name</label>
                                <input name="name" type="text" class="form-control" placeholder="name">
                            </div>
                            <div class="form-group">
                                <label class="sr-only">Username</label>
                                <input name="username" type="text" class="form-control" placeholder="username">
                            </div>
                            <button type="submit" class="btn btn-primary btn-lg">Launch</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>



   
</body>
</html>