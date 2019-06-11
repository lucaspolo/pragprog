(defn p
    "Select pen to write"
    [pen]
    println(str "Selecting pen " pen))

(defn d
    "Down the pen in paper"
    []
    println(str "Pen down"))

(defn w
    "Write a line to west"
    [cm]
    println(str "Draw west " cm " cm"))

(defn n
    "Write a line to north"
    [cm]
    println(str "Draw north " cm " cm"))

(defn e
    "Write a line to east"
    [cm]
    println(str "Draw east " cm " cm"))

(defn s
    "Write a line to south"
    [cm]
    println(str "Draw south " cm " cm"))

(defn u
    []
    println(str "Pen up"))