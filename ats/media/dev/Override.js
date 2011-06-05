Ext.override(Ext.form.TextField, {
    validateValue : function(value){
        if(Ext.isFunction(this.validator)){
            var msg = this.validator(value);
            if(msg !== true && !this.allowBlank){
                this.markInvalid(msg);
                return false;
            }
        }
        if(this.vtype){
            var vt = Ext.form.VTypes;
            if(!vt[this.vtype](value, this) && value.length > 0){
                this.markInvalid(this.vtypeText || vt[this.vtype +'Text']);
                return false;
            }
        }
        if(this.regex && !this.regex.test(value) && value.length > 0){
            this.markInvalid(this.regexText);
            return false;
        }
        if(value.length < 1 || value === this.emptyText){ // if it's blank
             if(this.allowBlank){
                 this.clearInvalid();
                 return true;
             }else{
                 this.markInvalid(this.blankText);
                 return false;
             }
        }
        if(value.length < this.minLength){
            this.markInvalid(String.format(this.minLengthText, this.minLength));
            return false;
        }
        if(value.length > this.maxLength){
            this.markInvalid(String.format(this.maxLengthText, this.maxLength));
            return false;
        }
        return true;
    }
});
