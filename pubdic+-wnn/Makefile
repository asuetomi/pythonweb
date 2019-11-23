#
# Makefile for pubdic+ dictionaries
#
#   Do simply 'make' for normal cases.
#

WNNBINDIR=/usr/local/bin/Wnn4
WNNWNNDIR=/usr/local/lib/wnn
JWNNWNNDIR=$(WNNWNNDIR)/ja_JP
JWNNDICDIR=$(JWNNWNNDIR)/dic

WNNOWNER=wnn

ATOD=$(WNNBINDIR)/atod
ATOF=$(WNNBINDIR)/atof
WNNTOUCH=${WNNBINDIR}/wnntouch
CPP=cpp
CHOWN=/usr/sbin/chown
DESTDIR=$(JWNNDICDIR)/pubdic+
HINSI=hinsi.data
FZK_SRC=\
	fzk.master \
	fzk.attr \
	fzk.jirattr \
	fzk.fzkattr \
	fzk.jircon \
	fzk.con \
	fzk.shuutan

FZK_FLAG=

DIC=\
	kihon.dic \
	setsuji.dic \
	jinmei.dic \
	chimei.dic \
	koyuu.dic \
	special.dic \
	computer.dic \
	bio.dic \
	symbol.dic \
	tankan.dic

FZK=\
	full.fzk \
	kougo.fzk \
	std.fzk

OBJ = $(DIC) $(FZK)

all: $(OBJ)

install: $(OBJ)
	@if [ ! -d $(DESTDIR) ] ; then mkdir $(DESTDIR) ; fi
	$(CHOWN) $(WNNOWNER) $(DESTDIR)
	install -c -o $(WNNOWNER) -m 644 $(OBJ) $(DESTDIR)
	@for file in $(OBJ); do \
	    $(WNNTOUCH) $(DESTDIR)/$$file; \
	done

local:
	-mkdir $(DEST_DIR)
	mv $(OBJ) $(DEST_DIR)

clean:
	rm -f *.fzk *.dic

std.fzk: $(FZK_SRC)
	$(CPP) $(FZK_FLAG) fzk.master | egrep -v '^(# |$$)' | $(ATOF) $@

full.fzk: $(FZK_SRC)
	make FZK_FLAG=-DKANSAI std.fzk
	mv std.fzk $@

kougo.fzk: $(FZK_SRC)
	make FZK_FLAG=-DKOUGO std.fzk
	mv std.fzk $@

.SUFFIXES: .hd .u .dic

.hd.dic: 
	cat  $< $*.u | $(ATOD) -p Version -P Version $@

.u.dic: 
	cat $*.hd $< | $(ATOD) -p Version -P Version $@

$(DIC): $(HINSI)
