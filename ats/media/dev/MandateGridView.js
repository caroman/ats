/*
 * File: MandateGridView.js
 * Date: Fri Aug 06 2010 01:32:36 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

MandateGridView = Ext.extend(MandateGridViewUi, {
    constructor: function(cfg) {
        cfg = cfg || {};
        cfg["getRowClass"] = this.applyRowClass;
        MandateGridView.superclass.constructor.call(this, Ext.apply({
        }, cfg));
    }
    ,applyRowClass: function(record, rowIndex, p, ds) {
        var xf = Ext.util.Format;
        p.body = '<p>' + 
                 xf.ellipsis(xf.stripTags(record.data.responsability), 200) + 
                 '</p>';
        return 'x-grid3-row-expanded';
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
Ext.reg('mandategridview', MandateGridView);
