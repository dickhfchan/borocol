webpackJsonp([24],{GNO3:function(e,t){},KmAY:function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=s("7Xc1"),i=s("6Tc7"),l={extends:a.a,components:{DatePicker:i.a},data:function(){return{}},created:function(){this.$validate(this.validation,this.fields)}},o={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{class:"CreateCoursePage"+e.index},[s("div",{staticClass:"content-card"},[s("div",{staticClass:"content-card-header"},[s("div",{staticClass:"step"},[e._v("Step "+e._s(e.step))]),s("div",{staticClass:"title"},[e._v(e._s(e.title))])]),s("div",{staticClass:"content-card-progress-bar progress"},[s("div",{staticClass:"progress-bar progress-bar-warning",style:{width:e.progressStr},attrs:{role:"progressbar"}},[e._v(e._s(e.progressStr))])]),s("div",{staticClass:"content-card-body has-tips"},[s("form",{staticClass:"row"},[s("div",{staticClass:"_1 col-sm-12"},[s("div",{staticClass:"form-group"},[s("label",[e._v(e._s(e.fields.seats.required?"* ":"")+e._s(e.fields.seats.text))]),s("span",{staticClass:"question-circle icon icon-question-circle mlm"}),s("input",{directives:[{name:"model",rawName:"v-model",value:e.fields.seats.value,expression:"fields.seats.value"}],staticClass:"form-control mlm",attrs:{type:"number"},domProps:{value:e.fields.seats.value},on:{input:function(t){t.target.composing||e.$set(e.fields.seats,"value",t.target.value)}}})]),s("div",{staticClass:"form-group"},[s("label",[e._v(e._s(e.fields.price.required?"* ":"")+e._s(e.fields.price.text))]),s("span",{staticClass:"question-circle icon icon-question-circle mlm"}),s("input",{directives:[{name:"model",rawName:"v-model",value:e.fields.price.value,expression:"fields.price.value"}],staticClass:"form-control mlm",attrs:{type:"number"},domProps:{value:e.fields.price.value},on:{input:function(t){t.target.composing||e.$set(e.fields.price,"value",t.target.value)}}}),s("span",{staticClass:"help-block2 mlm grey"},[e._v("USD")])])]),s("div",{staticClass:"mtm"},[e._v(" ")]),s("div",{staticClass:"col-sm-6"},[s("div",{staticClass:"form-group"},[s("label",[e._v(e._s(e.fields.registrationStartDate.required?"* ":"")+e._s(e.fields.registrationStartDate.text))]),s("DatePicker",{model:{value:e.fields.registrationStartDate.value,callback:function(t){e.$set(e.fields.registrationStartDate,"value",t)},expression:"fields.registrationStartDate.value"}})],1)]),s("div",{staticClass:"col-sm-6"},[s("div",{staticClass:"form-group"},[s("label",[e._v(e._s(e.fields.registrationEndDate.required?"* ":"")+e._s(e.fields.registrationEndDate.text))]),s("DatePicker",{model:{value:e.fields.registrationEndDate.value,callback:function(t){e.$set(e.fields.registrationEndDate,"value",t)},expression:"fields.registrationEndDate.value"}})],1)]),s("div",{staticClass:"form-group col-sm-12 additional"},[e._m(0),s("div",{staticClass:"line1 mtm"},[s("Checkbox",{model:{value:e.fields.earlyBirdDiscount.value,callback:function(t){e.$set(e.fields.earlyBirdDiscount,"value",t)},expression:"fields.earlyBirdDiscount.value"}}),s("label",{staticClass:"mls"},[e._v("Early Bird Discount")]),s("span",{staticClass:"question-circle icon icon-question-circle mlm"}),s("label",{staticClass:"mll"},[e._v("Discount Rate")]),s("select",{directives:[{name:"model",rawName:"v-model",value:e.fields.discountRate.value,expression:"fields.discountRate.value"}],staticClass:"form-control mls",on:{change:function(t){var s=Array.prototype.filter.call(t.target.options,function(e){return e.selected}).map(function(e){return"_value"in e?e._value:e.value});e.$set(e.fields.discountRate,"value",t.target.multiple?s:s[0])}}},[s("option",{domProps:{value:null}},[e._v("Please select")]),s("option",[e._v("10% off copy")]),s("option",[e._v("20% off copy")])]),s("label",{staticClass:"mll"},[e._v("Quota")]),s("select",{directives:[{name:"model",rawName:"v-model",value:e.fields.quota.value,expression:"fields.quota.value"}],staticClass:"form-control mls",on:{change:function(t){var s=Array.prototype.filter.call(t.target.options,function(e){return e.selected}).map(function(e){return"_value"in e?e._value:e.value});e.$set(e.fields.quota,"value",t.target.multiple?s:s[0])}}},[s("option",{domProps:{value:null}},[e._v("Please select")]),s("option",[e._v("10% off copy")]),s("option",[e._v("20% off copy")])])],1),s("div",{staticClass:"line2"},[s("Checkbox",{model:{value:e.fields.downPayment.value,callback:function(t){e.$set(e.fields.downPayment,"value",t)},expression:"fields.downPayment.value"}}),s("label",{staticClass:"mls"},[e._v("Down Payment 25%")]),s("span",{staticClass:"question-circle icon icon-question-circle mlm"})],1)])]),s("Tips")],1)])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"dividing-line-title mtl"},[t("div",{staticClass:"line"}),t("div",{staticClass:"mhm"},[this._v("Additional")]),t("div",{staticClass:"line"})])}]},r=s("8AGX")(l,o,!1,function(e){s("GNO3")},null,null);t.default=r.exports}});