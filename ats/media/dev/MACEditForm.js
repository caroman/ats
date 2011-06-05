/*
 * File: MACEditForm.js
 * Date: Thu Aug 12 2010 21:16:59 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

MACEditForm = Ext.extend(MACEditFormUi, {
    initComponent: function() {
        MACEditForm.superclass.initComponent.call(this);

        this.updatebutton.on('click', this.onUpdateClick, this );
        this.createbutton.on('click', this.onCreateClick, this );
    }
    ,markReadOnlyFields: function ( fields ) {
        var form = this.getForm();
        for (name in fields){
            var field = form.findField( name );
            if ( !Ext.isEmpty( field ) ) {
                field.readOnly = fields[ name ];
                field.editable = !fields[ name ];
            }
        }
    }
    ,populateRecord: function ( record ) {
        var form = this.getForm();
        form.reset();
    	form.loadRecord( record );
        if ( !Ext.isEmpty( record.data.id ) ) {
            form.findField('id').setValue( record.data['id'] );
        }
        if ( !Ext.isEmpty( record.data.activity ) ) {
            form.findField('activity').setValue( record.data.activity['pk'] );
        }
        if ( !Ext.isEmpty( record.data.status ) ) {
            form.findField('status').setValue( record.data.status['pk'] );
        }
        if ( !Ext.isEmpty( record.data.candidate ) ) {
            form.findField('candidate').setValue( record.data.candidate['pk'] );
        }
        if ( !Ext.isEmpty( record.data.mandate ) ) {
            form.findField('mandate').setValue( record.data.mandate['pk'] );
        }
    }
    ,onUpdateClick: function( button, event ) {
        this.fbar.disable();
        var form = this.getForm();
        if( form.isValid() ){
            form.submit({
                url: '/ats/main/mac/update/'
                ,scope: this
                ,waitMsg: 'Updating mac...'
                ,success: this.onSuccess
                ,failure: this.onFailure
            });
        }
    }
    ,onCreateClick: function( button, event ) {
        this.fbar.disable();
        var form = this.getForm();
        if( form.isValid() ){
            form.submit({
                url: '/ats/main/mac/new/'
                ,scope: this
                ,waitMsg: 'Creating new event...'
                ,success: this.onSuccess
                ,failure: this.onFailure
            });
        }
    }
    ,onSuccess: function( form, action ) {
        Ext.StoreMgr.lookup('MACStore').reload();
        Ext.example.msg('Success','Event upated correctly".');
        //close window
        this.fbar.enable();
        if ( this.ownerCt.closable ) {
            this.ownerCt.close();
        }
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
        this.fbar.enable();
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
Ext.reg('maceditform', MACEditForm);
