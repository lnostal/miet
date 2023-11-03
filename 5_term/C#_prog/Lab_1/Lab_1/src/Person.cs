public class Person{
    private string _name;
    private string _surname;
    private DateTime _birthday;

    public Person(string name, string surname, DateTime birthday){
        _name = name;
        _surname = surname;
        _birthday = birthday;
    }

    public Person(){
        _name = "John";
        _surname = "Doe";
        _birthday = DateTime.Now;
    }

    public string Name {
        get { return _name; }
        set { _name = value; }
    }

    public string Surname {
        get { return _surname; }
        set { _surname = value; }
    }

    public DateTime Birthday {
        get { return _birthday; }
        set { _birthday = value; }
    }

    public int BirthYear {
        get { return _birthday.Year; }
        set { _birthday = new DateTime(value, _birthday.Month, _birthday.Day); }
    }

    public override string ToString() {
        return String.Format("class <{0}>:\n\tname:\t\t{1}\n\tsurname:\t{2}\n\tbirthay:\t{3}",base.ToString(), _name, _surname, _birthday);
    }

    public virtual string ToShortString() {
        return String.Format("{0} {1}", _name, _surname);
    }

}


