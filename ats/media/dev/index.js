/*
 * File: xds_index.js
 * Date: Thu Sep 30 2010 00:02:25 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

Ext.onReady(function() {
    Ext.QuickTips.init();
    var cmp1 = new ATS({
        renderTo: Ext.getBody()
    });
    cmp1.show();

    Ext.StoreMgr.lookup('CandidateStore').load();
    Ext.StoreMgr.lookup('MandateStore').load();
    Ext.StoreMgr.lookup('MACStore').load();
    Ext.StoreMgr.lookup('MandateStatusStore').load();
    Ext.StoreMgr.lookup('MACStatusStore').load();
    Ext.StoreMgr.lookup('ActivitiesStore').load();
    Ext.StoreMgr.lookup('HiringManagerStore').load();
    Ext.StoreMgr.lookup('ManagmentExperienceStore').load();
    Ext.StoreMgr.lookup('ProfessionalDesignationStore').load();
    Ext.StoreMgr.lookup('WorkTypeStore').load();
    Ext.StoreMgr.lookup('WorkLocationStore').load();
    Ext.StoreMgr.lookup('CandidateComboBoxStore').load();
    Ext.StoreMgr.lookup('MandateComboBoxStore').load();
});
