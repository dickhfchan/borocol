webpackJsonp([7],{iSRw:function(e,s){},sGvR:function(e,s,t){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var a={extends:t("7Xc1").a,data:function(){return{}},created:function(){this.$validate(this.validation,this.fields)}},i={render:function(){var e=this,s=e.$createElement,t=e._self._c||s;return t("div",{class:"CreateCoursePage"+e.index},[t("div",{staticClass:"content-card"},[t("div",{staticClass:"content-card-header"},[t("div",{staticClass:"step"},[e._v("Step "+e._s(e.step))]),t("div",{staticClass:"title"},[e._v(e._s(e.title))])]),t("div",{staticClass:"content-card-progress-bar progress"},[t("div",{staticClass:"progress-bar progress-bar-warning",style:{width:e.progressStr},attrs:{role:"progressbar"}},[e._v(e._s(e.progressStr))])]),t("div",{staticClass:"content-card-body has-tips"},[t("form",[t("div",{staticClass:"form-group"},[t("label",[e._v(e._s(e.fields.guestRequirement.required?"* ":"")+e._s(e.fields.guestRequirement.text))]),t("textarea",{directives:[{name:"model",rawName:"v-model",value:e.fields.guestRequirement.value,expression:"fields.guestRequirement.value"}],staticClass:"form-control",attrs:{rows:"3",placeholder:"- Skill level\n- Occupations"},domProps:{value:e.fields.guestRequirement.value},on:{input:function(s){s.target.composing||e.$set(e.fields.guestRequirement,"value",s.target.value)}}})]),t("div",{staticClass:"form-group"},[t("label",[e._v(e._s(e.fields.requestFormExisted.required?"* ":"")+e._s(e.fields.requestFormExisted.text))]),t("CheckboxGroup",{attrs:{multiple:!1},model:{value:e.fields.requestFormExisted.value,callback:function(s){e.$set(e.fields.requestFormExisted,"value",s)},expression:"fields.requestFormExisted.value"}},[t("Checkbox",{staticClass:"mls",attrs:{value:!1}}),t("span",{staticClass:"mls"},[e._v("No")]),t("Checkbox",{staticClass:"mls",attrs:{value:!0}}),t("span",{staticClass:"mls"},[e._v("Yes")])],1)],1),t("div",{staticClass:"_1"},e._l(e.fields.requestForm.value,function(s,a){return t("div",{staticClass:"form-group"},[t("Checkbox",{model:{value:s.enabled,callback:function(t){e.$set(s,"enabled",t)},expression:"item.enabled"}}),t("span",{staticClass:"mls"},[e._v("Question "+e._s(a+1)+" :")]),t("textarea",{directives:[{name:"model",rawName:"v-model",value:s.value,expression:"item.value"}],staticClass:"form-control mls",attrs:{rows:"3"},domProps:{value:s.value},on:{input:function(t){t.target.composing||e.$set(s,"value",t.target.value)}}}),t("div",{staticClass:"clearfix"})],1)}))]),t("Tips")],1)])])},staticRenderFns:[]},r=t("8AGX")(a,i,!1,function(e){t("iSRw")},null,null);s.default=r.exports}});
//# sourceMappingURL=7.98db3108375267cf2f3d.js.map