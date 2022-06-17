from django.db import models


class Absences(models.Model):
    idabsences = models.IntegerField(db_column='idAbsences', primary_key=True)  # Field name made lowercase.
    idetudiants = models.ForeignKey('Etudiants', models.DO_NOTHING, db_column='idEtudiants')  # Field name made lowercase.
    idcours = models.ForeignKey('Cours', models.DO_NOTHING, db_column='idCours')  # Field name made lowercase.
    jutsificationcours = models.BooleanField(db_column='JutsificationCours')  # Field name made lowercase.
    docjustcours = models.ImageField(db_column='DocjustCours', max_length=255, upload_to="images/")  # Field name made lowercase.

    def __str__(self):
        return f"Justifié : {self.jutsificationcours}"

    class Meta:
        managed = False
        db_table = 'absences'


class Cours(models.Model):
    idcours = models.IntegerField(primary_key=True)
    titrecours = models.CharField(db_column='TitreCours', max_length=45)  # Field name made lowercase.
    datecours = models.DateField(db_column='DateCours')  # Field name made lowercase.
    idenseignants = models.ForeignKey('Enseignants', models.DO_NOTHING, db_column='idEnseignants')  # Field name made lowercase.
    dureecours = models.CharField(db_column='DureeCours', max_length=45)  # Field name made lowercase.
    idgroupe = models.ForeignKey('GroupeEtudiant', models.DO_NOTHING, db_column='idGroupe')  # Field name made lowercase.

    def __str__(self):
        return f"{self.titrecours} {self.dureecours}"

    class Meta:
        managed = False
        db_table = 'cours'


class Enseignants(models.Model):
    idenseignants = models.IntegerField(db_column='idEnseignants', primary_key=True)  # Field name made lowercase.
    nomenseignants = models.CharField(db_column='NomEnseignants', max_length=45)  # Field name made lowercase.
    prenomenseignants = models.CharField(db_column='PrenomEnseignants', max_length=45)  # Field name made lowercase.
    emailenseignants = models.EmailField(db_column='EmailEnseignants', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return f"{self.nomenseignants} {self.prenomenseignants}"

    class Meta:
        managed = False
        db_table = 'enseignants'


class Etudiants(models.Model):
    idetudiants = models.IntegerField(primary_key=True)
    nometudiants = models.CharField(db_column='NomEtudiants', max_length=25)  # Field name made lowercase.
    prenometudiant = models.CharField(db_column='PrenomEtudiant', max_length=25)  # Field name made lowercase.
    emailetudiant = models.EmailField(db_column='EmailEtudiant', max_length=45)  # Field name made lowercase.
    idgroupee = models.ForeignKey('GroupeEtudiant', models.DO_NOTHING, db_column='idGroupeE')  # Field name made lowercase.
    photoetudiant = models.ImageField(db_column='PhotoEtudiant', max_length=255, upload_to="images/")  # Field name made lowercase.

    def __str__(self):
        return f"{self.nometudiants} {self.prenometudiant}"

    class Meta:
        managed = False
        db_table = 'etudiants'


class GroupeEtudiant(models.Model):
    idgroupe_etudiant = models.IntegerField(db_column='idGroupe-etudiant', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomgroupe_etudiant = models.CharField(db_column='nomGroupe-etudiant', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return f"{self.nomgroupe_etudiant}"

    class Meta:
        managed = False
        db_table = 'groupe-etudiant'