% rebase('osnova.tpl')
<h1>Create your character!</h1>
    <p>Tell me more about {{ ch_name }}.</p>
    <form action='/cci-post/' method="POST">
        Race: <input type="text" name="ch_race">
        Subrace: <input type="text" name="ch_subrace">
        Class: <input type="text" name="ch_class">
        Subclass: <input type="text" name="ch_subclass">
        Backgroung: <input type="text" name="ch_background">
        <input type="submit" value="Create!">
    </form>