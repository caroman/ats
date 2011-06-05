/*
 * File: MandateMACGridView.js
 * Date: Sun Apr 03 2011 22:59:38 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

MandateMACGridView = Ext.extend(MandateMACGridViewUi, {
    constructor: function(cfg) {
        cfg = cfg || {};
        cfg["getRowClass"] = this.applyRowClass;
        MandateMACGridView.superclass.constructor.call(this, Ext.apply({
        }, cfg));
    }
    ,applyRowClass: function(record, rowIndex, p, ds) {
        if ( !Ext.isDate( record.data["date"] ) ){
            return '';
        } else if ( !Ext.isEmpty( record.data["status"] ) && 
                    ( record.data["status"]["fields"]["title"] == 'Complete' || 
                      record.data["status"]["fields"]["title"] == 'Cancel' )  )  {
            return '';
        }
        var today = new Date();
        var today_date = new Date( today.getFullYear(),
                                   today.getMonth(),
                                   today.getDate() );
        var mac_date = new Date( record.data["date"].getFullYear(),
                                 record.data["date"].getMonth(),
                                 record.data["date"].getDate() );

        var delta_days = parseInt( (mac_date - today_date) / 86400000 );

        if ( delta_days > 0 ){
            return 'mac-future-row';
        } else if ( delta_days == 0 ) {
            return 'mac-present-row';
        } else {
            return 'mac-past-row';
        }
    }
    /*
    Overwrite onHeaderClick private function of View to capture ID of column
    instead of the DataIndex. 
    */
    ,onHeaderClick : function(g, index){
        if(this.headersDisabled || !this.cm.isSortable(index)){
            return;
        }
        if (g.store.remoteSort) {
            g.stopEditing(true);
            var name = this.cm.getColumnId(index);
            if (typeof name === 'number' ) {
                name = this.cm.getDataIndex(index);
            }
            if (typeof name === 'undefined' ) return false;

            var sortInfo   = g.store.sortInfo || null;

            var dir = 'ASC';
            if (sortInfo && sortInfo.field == name) { // toggle sort dir
                dir = (g.store.sortToggle[name] || 'ASC').toggle('ASC', 'DESC');
            } 

            g.store.sortToggle[name] = dir;
            g.store.sortInfo = {field: name, direction: dir};
            g.store.hasMultiSort = false;

            if (!g.store.load(g.lastOptions)) {
                if (sortToggle) {
                    g.store.sortToggle[name] = sortToggle;
                }
                if (sortInfo) {
                    g.store.sortInfo = sortInfo;
                }
            }
            this.updateSortIcon(index, dir);
        } else { 
            g.stopEditing(true);
            g.store.sort(this.cm.getDataIndex(index));
        }
    }
});
Ext.reg('mandatemacgridview', MandateMACGridView);
