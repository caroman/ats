from django.db import models

################################################################################
class Activity( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the activities' )
    title = models.CharField(
        max_length = 25,
        help_text = 'Title of the activity' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

################################################################################
class HiringManager( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    name = models.CharField(
        null = True,
        blank = True,
        max_length = 50,
        help_text = 'Name of the hiring manager' )

    def __unicode__(self):
        return u"%s" % (self.name,)

    class Meta:
        ordering = ['priority','name']
        verbose_name = 'Hiring Manager'
        verbose_name_plural = 'Hiring Managers'


################################################################################
class MACStatus( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    title = models.CharField(
        max_length = 25,
        help_text = 'Title of the status' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'MAC Status'
        verbose_name_plural = 'MAC Status'

################################################################################
class ManagmentExperience( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    title = models.CharField(
        max_length = 25,
        help_text = 'Level of managment' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'Managment Experience'
        verbose_name_plural = 'Managment Experiences'

################################################################################
class MandateStatus( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    title = models.CharField(
        max_length = 25,
        help_text = 'Title of the status' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'Mandate Status'
        verbose_name_plural = 'Mandate Status'


################################################################################
class ProfessionalDesignation( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    title = models.CharField(
        max_length = 50,
        help_text = 'Professional designation' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'Professional Designation'
        verbose_name_plural = 'Professional Designations'

################################################################################
class WorkLocation( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    title = models.CharField(
        max_length = 25,
        help_text = 'Prefered work location' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'Work Location'
        verbose_name_plural = 'Work Locations'

################################################################################
class WorkType( models.Model ):
    priority = models.PositiveIntegerField(
        default = None,
        null = True,
        blank = True,
        help_text = 'Number used to sort the list' )
    title = models.CharField(
        max_length = 25,
        help_text = 'Prefered work type' )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['priority','title']
        verbose_name = 'Work Type'
        verbose_name_plural = 'Work Types'


################################################################################

