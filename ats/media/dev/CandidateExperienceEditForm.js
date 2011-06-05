/*
 * File: CandidateExperienceEditForm.js
 * Date: Wed Oct 27 2010 01:02:42 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

CandidateExperienceEditForm = Ext.extend(CandidateExperienceEditFormUi, {
    initComponent: function() {
            CandidateExperienceEditForm.superclass.initComponent.call(this);

            this.cbprofessionaldesignations = new Ext.ux.form.SuperBoxSelect({
                allowBlank:true,
                xtype:'superboxselect',
                fieldLabel: 'Professional Designations',
                resizable: true,
                name: 'professional_designations',
                anchor:'100%',
                store: { xtype: 'professionaldesignationstore' },
                mode: 'local',
                displayField: 'title',
                displayFieldTpl: '{title}',
                valueField: 'id',
                //value: '',
                forceSelection : false
            });
    
            this.cbworklocations = new Ext.ux.form.SuperBoxSelect({
                allowBlank:true,
                xtype:'superboxselect',
                fieldLabel: 'Work Locations',
                resizable: true,
                name: 'work_locations',
                anchor:'100%',
                store: { xtype: 'worklocationstore' },
                mode: 'local',
                displayField: 'title',
                displayFieldTpl: '{title}',
                valueField: 'id',
                //value: '',
                forceSelection : false
            });
    
            this.cbworktypes = new Ext.ux.form.SuperBoxSelect({
                allowBlank:true,
                xtype:'superboxselect',
                fieldLabel: 'Work Types',
                resizable: true,
                name: 'work_types',
                anchor:'100%',
                store: { xtype: 'worktypestore' },
                mode: 'local',
                displayField: 'title',
                displayFieldTpl: '{title}',
                valueField: 'id',
                //value: '',
                forceSelection : false
            });
    
            this.updatebutton.on('click', this.onUpdateClick, this );
            this.createbutton.on('click', this.onCreateClick, this );
        }
        ,populateRecord: function( record ) {
            var form = this.getForm();
            form.loadRecord( record );
            //load select
            if ( record.data.managment_experience != null ) {
                form.findField('managment_experience').setValue(
                    record.data.managment_experience['pk'] 
                );
            }
            //load multiselect
            form.findField('professional_designations').setValue(
               Ext.pluck( record.data.professional_designations , 'pk').toString()
            ); 
            form.findField('work_locations').setValue(
               Ext.pluck( record.data.work_locations, 'pk').toString()
            ); 
            form.findField('work_types').setValue(
               Ext.pluck( record.data.work_types, 'pk').toString()
            ); 
        }
        ,onRender: function(ct, position) {
            CandidateExperienceEditForm.superclass.onRender.call(this, ct, position);
            this.add( this.cbprofessionaldesignations );
            this.add( this.cbworktypes );
            this.add( this.cbworklocations );
        }
        ,onUpdateClick: function( button, event ) {
            var form = this.getForm();
            if( form.isValid() ){
                form.submit({
                     url: '/ats/main/candidate/update/experience/'
                    ,scope: this
                    ,waitMsg: 'Updating candidate...'
                    ,success: this.onSuccess
                    ,failure: this.onFailure
                });
            }
        }
        ,onCreateClick: function( button, event ) {
            var form = this.getForm();
            if( form.isValid() ){
                form.submit({
                    url: '/ats/main/candidate/new/'
                    ,scope: this
                    ,waitMsg: 'Creating new candidate...'
                    ,success: this.onSuccess
                    ,failure: this.onFailure
                });
            }
        }
        ,onSuccess: function( form, action ) {
            //Ext.StoreMgr.lookup('CandidateStore').reload();
            Ext.example.msg('Success','Candidated upated correctly".');
            //Ext.Msg.show({
            //    title: 'Success'
            //    ,msg: 'Candidate updated succesfully!'
            //    ,modal: true
            //    ,icon: Ext.Msg.INFO
            //    ,buttons: Ext.Msg.OK
            //});
        }
        ,onFailure: function( form, action ) {
            switch ( action.failureType ) {
                case Ext.form.Action.CLIENT_INVALID:
                    this.onClientInvalid( form, action);
                break;
                case Ext.form.Action.CONNECT_FAILURE:
                    this.onConnectionFailure(form, action);
                break;
                case Ext.form.Action.SERVER_INVALID:
                    this.onServerInvalid(form, action);
                break;
            };
        }
        ,onClientInvalid: function( form, action ) {
            Ext.Msg.alert('Failure',
                          'Fields may not be submitted with invalid values');
        } 
        ,onConnectionFailure: function( form, action ) {
            Ext.Msg.alert('Failure', 
                          'Ajax communication failed');
        }
        ,onServerInvalid: function( form, action ) {
            Ext.Msg.alert('Failure', action.result.msg);
        }
});
Ext.reg('candidateexperienceeditform', CandidateExperienceEditForm);