/*
 * File: CandidateComboBox.js
 * Date: Fri Aug 13 2010 01:39:57 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.11.
 * http://www.extjs.com/products/designer/
 *
 * This file will be generated the first time you export.
 *
 * You should implement event handling and custom methods in this
 * class.
 */

CandidateComboBox = Ext.extend(CandidateComboBoxUi, {
    initComponent: function() {
        CandidateComboBox.superclass.initComponent.call(this);
    }
    ,setValue: function (v) {

        // Store not loaded yet? Set value when it *is* loaded.
        // Defer the setValue call until after the next load.
        if (this.store.getCount() == 0) {
            this.store.on('load',
                this.setValue.createDelegate(this, [v]), null, {single: true});
            return;
        }
        var text = v;
        if(this.valueField){
            var r = this.findRecord(this.valueField, v);
            if(r){
                text = 'ID:' + r.data[this.displayField] + ' ' +
                       r.data['first_name'] + ' ' +
                       r.data['last_name'];
            }else if(this.valueNotFoundText !== undefined){
                text = this.valueNotFoundText;
            }
        }
        this.lastSelectionText = text;
        if(this.hiddenField){
            this.hiddenField.value = v;
        }
        CandidateComboBox.superclass.setValue.call(this, text);
        this.value = v;
        this.hiddenField.value = v;
    }
});
Ext.reg('candidatecombobox', CandidateComboBox);
