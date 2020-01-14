<script>
function Ninja(name, health) {
    var speed = "3";
    var strength = "3;"
    var privateMethod = function() {
        console.log(this);
    }
    this.name = name;
    this.health = health;
    this.sayName = function() {
        console.log(" my name is " + this.name + " my health " + this.health + " points!");
    }
    this.showStats = function() {
        console.log(" name: " + this.name + " strength: " + strength + " speed:" + speed + " health:" + this.health );
        privateMethod();
    }
    this.drinkSake = function(){
        this.health +=10;
        return this;
    }
}
var ninja1 = new Ninja("Shinobi", 100);
ninja1.sayName();
ninja1.showStats();
ninja1.drinkSake();
    </script>
</head>
<body>
    
</body>
</html>
