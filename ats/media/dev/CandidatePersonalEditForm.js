/*
 * File: CandidatePersonalEditForm.js
 * Date: Sun Aug 01 2010 22:43:02 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

CandidatePersonalEditForm = Ext.extend(CandidatePersonalEditFormUi, {
    initComponent: function() {
        CandidatePersonalEditForm.superclass.initComponent.call(this);
 
        this.updatebutton.on('click', this.onUpdateClick, this );
        this.createbutton.on('click', this.onCreateClick, this );
    }
    ,populateRecord: function ( record ) {
        var form = this.getForm();
        form.reset();
        form.loadRecord( record );
    }
    ,onRender: function(ct, position) {
        CandidatePersonalEditForm.superclass.onRender.call(this, ct, position);
    }
    ,onUpdateClick: function( button, event ) {
        var form = this.getForm();
        if( form.isValid() ){
            form.submit({
                 url: '/ats/main/candidate/update/personal/'
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
        //    ,msg: 'Candidated updated succesfully!'
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
                      'Form fields may not be submitted with invalid values');
    } 
    ,onConnectionFailure: function( form, action ) {
        Ext.Msg.alert('Failure', 
                      'Ajax communication failed');
    }
    ,onServerInvalid: function( form, action ) {
        Ext.Msg.alert('Failure', action.result.msg);
    }
    
});
Ext.reg('candidatepersonaleditform', CandidatePersonalEditForm);
