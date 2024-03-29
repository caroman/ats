/*
 * File: CandidateMACGrid.js
 * Date: Wed Mar 30 2011 20:30:01 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

CandidateMACGrid = Ext.extend(CandidateMACGridUi, {
    initComponent: function() {
        CandidateMACGrid.superclass.initComponent.call(this);

        //Template to display in any panel from a record of this.grid
        this.infotpl = new Ext.XTemplate(
            '<tpl for="."> <div class="preview">',
            ' <div class="info-data">',
            '  <span class="info-date">{date:date("M j, Y")}</span>',
            '  <tpl if="mandate"><tpl for="mandate.fields">',
            '      <h3 class="info-title">{title}</h3>',
            '  </tpl></tpl>',
            '  <tpl if="status"><tpl for="status.fields">',
            '   <h4 class="info-header">Status {title}</h4>',
            '  </tpl></tpl>',
            '  <tpl if="activity"><tpl for="activity.fields">',
            '   <h4 class="info-header">Activity {title}</h4>',
            '  </tpl></tpl>',
            ' </div>',
            ' <div class="info-body">{description}</div>',
            '</div></tpl>',
            {
                compiled: true
            }
            );

        this.newbutton.on('click', this.onNewClick, this );
        this.editbutton.on('click', this.onEditClick, this );
    }
    ,onRender: function(ct, position) {
        CandidateMACGrid.superclass.onRender.call(this, ct, position);
        this.applyColumnMandateRenderer( this );
        this.applyColumnActivityRenderer( this );
        this.applyColumnStatusRenderer( this );
    }
    ,onNewClick: function ( button, event ){
        var candidate__id = this.store.baseParams["candidate__id"];
        if ( !Ext.isEmpty( candidate__id ) ){
            var win = new MACNewWindow();
            //personalize title for candidate
            win.setTitle( win.title + " CANDIDATE " + candidate__id ); 
            //set to upload file and assign to this candidate
            var field = win.form.getForm().findField( 'candidate' );
            field.setValue( candidate__id );
            field.readOnly = true;
            field.editable = false;
            win.show();
        } else {
            Ext.Msg.alert('Warning','Candidate must be selected');
        }
    }
    ,onEditClick: function ( button, event ){
        var record = this.selModel.getSelected();
        var candidate__id = this.store.baseParams["candidate__id"];

        if ( !Ext.isEmpty( candidate__id ) && !Ext.isEmpty( record ) ){
            var win = new MACEditWindow();

            //personalize title for candidate
            win.setTitle( win.title + " CANDIDATE " + candidate__id );
            if ( !Ext.isEmpty( record.data.mandate ) ) {
                win.setTitle( win.title + " MANDATE " + 
                              record.data.mandate.fields.title );
            }

            //set to upload file and assign to this candidate
            var formpanel = win.items.itemAt(0);
    	    formpanel.populateRecord( record );
            formpanel.markReadOnlyFields( {'candidate': true, 'mandate': true} );
            win.show();
         } else {
            Ext.Msg.alert('Warning','Event must be selected');
        }
    }
    ,onSortChange: function( grid, sortInfo ) {
    }
    ,onContextClick : function( grid, index, e ){
    }
    ,setQuery: function ( query ){
    }
    ,applyColumnMandateRenderer: function ( grid ) {
        var cm = grid.getColumnModel();
        var column = null;
        //madate__title
        column = cm.getColumnById('mandate__title');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty( value ) ) {
                    return value['fields']['title'];
                }
            } 
        }
     }
    ,applyColumnStatusRenderer: function ( grid ) {
        var cm = grid.getColumnModel();
        var column = null;
        //status__title
        column = cm.getColumnById('status__title');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty( value ) ) {
                    return value['fields']['title'];
                }
            } 
        }
     }
     ,applyColumnActivityRenderer: function ( grid ) {
        var cm = grid.getColumnModel();
        var column = null;
        //status__title
        column = cm.getColumnById('activity__title');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty( value ) ) {
                    return value['fields']['title'];
                }
            } 
        }
     }
});
Ext.reg('candidatemacgrid', CandidateMACGrid);
