webpackJsonp([5],{"0aBE":function(t,s){},"4bCq":function(t,s,e){"use strict";var i={mixins:[e("ZXXD").a],props:{title:{}},data:function(){return{style:{left:null,display:""}}},watch:{title:{immediate:!0,handler:function(t){var s=this;this.mounted.then(function(){s.style.display="block",s.$nextTick(function(){var t=s.$refs.tip.offsetWidth;s.style.left=(s.$el.offsetWidth-t)/2+"px",s.style.display=""})})}}}},n={render:function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"Popover"},[this._t("default"),s("div",{ref:"tip",staticClass:"popover bottom",style:this.style},[s("div",{staticClass:"arrow"}),this.title?s("h3",{staticClass:"popover-title"},[this._v(this._s(this.title))]):this._e(),s("div",{staticClass:"popover-content"},[this._t("content")],2)])],2)},staticRenderFns:[]},a=e("8AGX")(i,n,!1,function(t){e("0aBE")},null,null);s.a=a.exports},Dq4q:function(t,s,e){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var i={components:{Popover:e("4bCq").a},data:function(){return{photos:[]}}},n={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"RequestRefund"},[s("div",{staticClass:"container"},[s("div",{staticClass:"content-card has-close"},[s("div",{staticClass:"title"},[this._v("Request Refund")]),s("form",{staticClass:"content-card-body"},[s("div",{staticClass:"form-group"},[s("label",[this._v("Please state your request reason:")]),s("textarea",{staticClass:"form-control",attrs:{rows:"15"}}),s("button",{staticClass:"send-btn btn btn-primary btn-lg mtl pull-right"},[this._v("Send")]),s("div",{staticClass:"clearfix"})])]),s("span",{staticClass:"icon icon-close close"})])])])}]},a=e("8AGX")(i,n,!1,function(t){e("mHcH")},null,null);s.default=a.exports},mHcH:function(t,s){}});
//# sourceMappingURL=5.ed86a926a4b3b3974611.js.map