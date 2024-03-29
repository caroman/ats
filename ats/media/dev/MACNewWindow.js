/*
 * File: MACNewWindow.js
 * Date: Thu Aug 12 2010 22:38:43 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

MACNewWindow = Ext.extend(MACNewWindowUi, {
    initComponent: function() {
        MACNewWindow.superclass.initComponent.call(this);

        this.cancelbutton.on('click', this.onCancelClick, this );
        this.createbutton.on('click', this.onCreateClick, this );
    }
    ,onCancelClick: function( button, event ) {
         this.close();
    }
    ,onCreateClick: function( button, event ) {
        var form = this.form.getForm();
        if( form.isValid() ){
            form.submit({
                url: '/ats/main/mac/new/'
                ,scope: this
                ,waitMsg: 'Creating new MAC...'
                ,success: this.onSuccess
                ,failure: this.onFailure
            });
        }
    }
    ,onSuccess: function( form, action ) {
        Ext.StoreMgr.lookup('MACStore').reload();
        Ext.example.msg('Success','MAC saved correctly".');
        //Ext.Msg.show({
        //    title: 'Success'
        //    ,msg: 'Reload grid to see new mac!'
        //    ,modal: true
        //    ,icon: Ext.Msg.INFO
        //    ,buttons: Ext.Msg.OK
        //});
        //close mac new window
        this.close();
    }
    ,onFailure: function( form, action ) {
        switch ( action.failureType ) {
            case Ext.form.Action.CLIENT_INVALID:
                this.onClientInvalid(form, action);
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
Ext.reg('macnewwindow', MACNewWindow);
