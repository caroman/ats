/*
 * File: MACGrid.js
 * Date: Mon Aug 09 2010 23:24:08 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

MACGrid = Ext.extend(MACGridUi, {
    initComponent: function() {
        MACGrid.superclass.initComponent.call(this);

        //searchfield in toolbar
        this.searchfield =  new Ext.ux.form.SearchField({
                 store: this.store
                 ,width: 350
            });

        //Template to display in any panel from a record of this.grid
        this.infotpl = new Ext.XTemplate(
            '<tpl for="."><div class="preview">',
            ' <div class="info-data">',
            '  <span class="info-date">{date:date("M j, Y")}</span>',
            '  <tpl if="mandate"><tpl for="mandate.fields">',
            '      <h3 class="info-title">{title}</h3>',
            '  </tpl></tpl>',
            '  <tpl if="candidate"><tpl for="candidate.fields">',
            '      <h3 class="info-title">{first_name} {last_name}</h3>',
            '      <tpl if="phone">',
            '       <h4 class="info-header">Phone {phone} Ext {phone_extension}</h4>',
            '      </tpl>',
            '      <tpl if="mobile">',
            '       <h4 class="info-header">Mobile {mobile}</h4>',
            '      </tpl>',
            '  </tpl></tpl>',
            '  <tpl if="status"><tpl for="status.fields">',
            '   <h4 class="info-header">Status {title}</h4>',
            '  </tpl></tpl>',
            '  <tpl if="activity"><tpl for="activity.fields">',
            '   <h4 class="info-header">Activity {title}</h4>',
            '  </tpl></tpl>',
            ' </div>',
            ' <div class="info-body">',
            '  <span><h3 class="info-title">Description</h3>{description}</span>',
            ' </div>',
            '</div></tpl>',
            {
                compiled: true
            }
            );

        //this.on('sortchange', this.onSortChange, this );
        this.newbutton.on('click', this.onNewClick, this );
        this.candidatebutton.on('click', this.onCandidateClick, this );
        this.mandatebutton.on('click', this.onMandateClick, this );
        this.extrafilterapplybutton.on('click', this.onExtraFilterApplyClick, this );
        this.extrafilterresetbutton.on('click', this.onExtraFilterResetClick, this );
    }
    ,onRender: function(ct, position) {
        MACGrid.superclass.onRender.call(this, ct, position);
        this.getTopToolbar().add(
             '->'
            ,'Search'
            ,' ' 
            ,this.searchfield
            ,''
            );
        //column renderers
        this.applyColumnCandidateRenderer( this );
        this.applyColumnMandateRenderer( this );
        this.applyColumnActivityRenderer( this );
        this.applyColumnStatusRenderer( this );
        this.applyColumnRecruiterRenderer( this );

    }
    ,onContextClick : function( grid, index, e ){
        alert('onContextClick');
    }
    ,onNewClick: function ( button, event ){
        var win = new MACNewWindow();
        var selected = this.selModel.getSelected();
        if ( !Ext.isEmpty( selected ) ){
            if ( !Ext.isEmpty( selected.data["candidate"] ) ){
                win.form.getForm().findField('candidate').setValue( 
                    selected.data["candidate"]["pk"]
                );
            }
            if ( !Ext.isEmpty( selected.data["mandate"] ) ){
                win.form.getForm().findField('mandate').setValue( 
                    selected.data["mandate"]["pk"]
                );
            }
        }
        win.show();
    }
    ,setQuery: function ( query ){
        this.searchfield.setQuery( query );
    }
    ,onCandidateClick: function ( button, event ){
        var selected = this.selModel.getSelected();
        if ( !Ext.isEmpty( selected ) ){
            candidate__id = selected.data["candidate"]['pk'];
            //must go in MainTabPanelClass
            var mainpanel =  Ext.getCmp('maintabpanel');
            mainpanel.activate( mainpanel.candidatetab );
            mainpanel.candidatetab.grid.setQuery(
                { 'candidate': candidate__id }
            );
         }
    }
    ,onMandateClick: function ( button, event ){
        var selected = this.selModel.getSelected();
        if ( !Ext.isEmpty( selected ) ){
            mandate__id = selected.data["mandate"]['pk'];
            //must go in MainTabPanelClass
            var mainpanel =  Ext.getCmp('maintabpanel');
            mainpanel.activate( mainpanel.mandatetab );
            mainpanel.mandatetab.grid.setQuery(
                { 'mandate': mandate__id }
            );
         }
    }
    ,onExtraFilterApplyClick: function ( button, event ){
        if ( !Ext.isEmpty( this.extrafilterfromdate.value ) ){
            this.store.setBaseParam('date>=',this.extrafilterfromdate.value );
        } else {
            delete this.store.baseParams["date>="];
        }
        if ( !Ext.isEmpty( this.extrafiltertodate.value ) ){
            this.store.setBaseParam('date<=',this.extrafiltertodate.value );
        } else {
            delete this.store.baseParams["date<="];
        }
        this.store.reload( this.store.lastOptions  );
    }
    ,onExtraFilterResetClick: function ( button, event ){
        this.extrafilterfromdate.reset();
        this.extrafiltertodate.reset();
        delete this.store.baseParams["date<="];
        delete this.store.baseParams["date>="];
        this.store.reload( this.store.lastOptions  );
    }
    ,applyColumnCandidateRenderer: function ( grid ) {
        var cm = grid.getColumnModel();
        var column = null;
        //candidate__id
        column = cm.getColumnById('candidate__id');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                var output = null;
                if ( !Ext.isEmpty(value) ) {
                    output = value['pk'];
                }
                return output;
            } 
        }
        //candidate__first_name
        column = cm.getColumnById('candidate__first_name');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty(value) ) {
                    return value['fields']['first_name'];
                }
            } 
        }
        //candidate__last_name
        column = cm.getColumnById('candidate__last_name');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty(value) ) {
                    return value['fields']['last_name'];
                }
            } 
        }
        //candidate__phone
        column = cm.getColumnById('candidate__phone');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty(value) ) {
                    return value['fields']['phone'] +
                           [ !Ext.isEmpty( value['fields']['phone_extension'] ) 
                            ? ' Ext.'+ value['fields']['phone_extension']
                            : '' ];
                }
            } 
        }
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
     ,applyColumnRecruiterRenderer: function ( grid ) {
        var cm = grid.getColumnModel();
        var column = null;
        //status__title
        column = cm.getColumnById('created_by__username');
        if ( !Ext.isEmpty( column ) ){
            column.renderer = function( value, cell ) {
                if ( !Ext.isEmpty( value ) ) {
                    return value['fields']['username'];
                }
            } 
        }
     }
 
});
Ext.reg('macgrid', MACGrid);
