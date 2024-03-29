/*
 * File: CandidateFileStore.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateFileStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        CandidateFileStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'CandidateFileStore',
            url: '/ats/main/candidatefile/list/',
            root: 'results',
            restful: true,
            fields: [
                {
                    name: 'title',
                    mapping: 'fields[\'title\']',
                    type: 'string'
                },
                {
                    name: 'download_link',
                    mapping: 'extras[\'download_link\']',
                    type: 'string'
                },
                {
                    name: 'created_time',
                    type: 'date',
                    dateFormat: 'Y-m-d h:m:s',
                    mapping: 'fields["created_time"]'
                },
                {
                    name: 'id',
                    type: 'int',
                    mapping: 'pk'
                }
            ]
        }, cfg));
    }
});
Ext.reg('candidatefilestore', CandidateFileStore);new CandidateFileStore();