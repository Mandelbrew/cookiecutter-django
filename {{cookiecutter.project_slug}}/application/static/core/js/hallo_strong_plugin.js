(function () {
    (function ($) {
        return $.widget('IKS.strong', {
            options: {
                uuid: '',
                tag: 'strong',
                editable: null,
                buttonCssClass: null
            },

            inContext: function () {
                var widget = this;
                var node = widget.options.editable.getSelection().commonAncestorContainer;
                return $(node).parents(widget.options.tag).get(0);
            },

            populateToolbar: function (toolbar) {

                var widget = this;
                var button = $('<span></span>');

                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    cssClass: this.options.buttonCssClass,
                    command: null,
                    label: 'Strong',
                    icon: 'icon-arrow-up',
                    queryState: function (event) {
                        return button.hallobutton('checked', !!widget.inContext());
                    }
                });

                // button.find('button .ui-button-text').text('STR');

                toolbar.append(button);

                button.on('click', function (event) {
                    if (widget.inContext()) {
                        return widget.options.editable.execute('removeFormat');
                    }

                    var lastSelection = widget.options.editable.getSelection();
                    var elem = "<" + widget.options.tag + ">" + lastSelection + "</" + widget.options.tag + ">";

                    var node = lastSelection.createContextualFragment(elem);

                    lastSelection.deleteContents();
                    lastSelection.insertNode(node);

                    return widget.options.editable.element.trigger('change');
                });
            }
        });
    })(jQuery);
}).call(this);