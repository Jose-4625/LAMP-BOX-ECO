<h1>ESP32-MicroPython Thermocycler / LAMP-Box</h1>

<h2>Deployment Files</h2>
<div>
===================================================================================
</div>
<p>
<b>Index.html contains</b>:{
  <div>
  <b>Libraries (embedded)</b>:<br>
  Bootstrap 4 CSS<br>
  Bootstrap 4 JS<br>
  jQuery<br>

  <b>Functionality:</b><br>
  HTML Table Parser<br>
  JSON string compiler<br>
  xmlHttpRequest server communication (GET/POST)<br>
  </div>

}

<b>LAMP.py contains</b>:{
  <div>
  <b>Libraries (imported)</b>:<br>
  MicroWebSrv2<br>
  time<br>
  json<br>
  RoutineInterfaceDataModel<br>

  <b>Functionality</b>:<br>
  creation of embedded device web server<br>
  web route handlers<br>
  JSON string to python Object converter<br>
  </div>
}
<br>
<b>RoutineInterfaceDataModel.py contains</b>:{
  <div>
  <b>Libraries (imported)</b>:<br>
  json<br>

  <b>Functionality</b>:<br>
  Handles the interpretation of json strings returning from the client.<br>
  Creates Routine Object from normal instantiation.(Discouraged)<br>
  Creation of single Routine object has <em>addSubRoutine</em> class method to allow multi-routine object creation and management(encouraged)<br>
  ex.

    from RoutineInterfaceDataModel import Routine

    jsonData = '{ClientRoutineJSONData}'

    Rout = Routine.addSubRoutine(jsonData) #creates Routine Obj and adds routine to static array
    #Routine automatically parses JSON into python Dict
    Rout.show() # print static array with all routine object that have been created

  </div>
}
<br>
<b>RTController.py contains</b>:{
  <div>
  <b>Libraries (imported)</b>:<br>
  RoutineInterfaceDataModel<br>
  time<br>
  gc<br>
  _thread<br>
  machine<br>
  max6677<br>

  <b>Functionality</b>:<br>
  Defines a minimal PID temperature controller<br>
  Defines an abstraction layer for interacting with ESP32 hardware<br>
  implementation of a Real-Time Controller Object to be an interface between the async webserver and async hardware functionality. All data between client and server hardware is called and passed through the RTController object.

  </div>
}
</p>

<h2>Non-Deployment Files</h2>
=================================================================================
<div>
<b>main.py</b> => MicroWebSrv2 Test file<br>
<b>gzipper.py</b> => file compressor<br>
<b>Build/uPyCompiler.py</b> => Python --> MicroPython bytecode compiler (RAM Optimization)<br>

</div>
