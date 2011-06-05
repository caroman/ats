/*
 * File: ATS.js
 * Date: Sat Jul 31 2010 07:31:27 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

ATS = Ext.extend(ATSUi, {
    initComponent: function() {
        ATS.superclass.initComponent.call(this);
        this.logoutButton.on('click', this.onLogOutButtonClick, this );
    }
    ,onLogOutButtonClick: function( button, event ){
        Ext.Msg.show({
            title :'Logout',
            msg : 'Continue with logging out ?',
            buttons : Ext.Msg.OKCANCEL,
            fn : this.processLogout,
            icon : Ext.MessageBox.QUESTION
        });
    }
    ,processLogout: function( btn ){
        if (btn == 'ok' ){
            self.location = '/ats/logout/' 
        }
    }
});
